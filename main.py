import os
import httpx
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("MODEL")
VOICE = os.getenv("VOICE")
if not OPENAI_KEY or not MODEL or not VOICE:
    raise RuntimeError("Missing environment variables. Ensure OPENAI_API_KEY, MODEL, and VOICE are set.")

@app.get("/session")
async def session():
    url = "https://api.openai.com/v1/realtime/sessions"
    headers = {
        "Authorization": f"Bearer {OPENAI_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"model": MODEL, "voice": VOICE}
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(url, json=payload, headers=headers, timeout=10.0)
        if resp.status_code != 200:
            try:
                err = resp.json()
            except:
                err = {"error": resp.text}
            raise HTTPException(status_code=resp.status_code, detail=err)
        return resp.json()
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail={"error": str(e)})

# Serve static files (frontend)
app.mount("/", StaticFiles(directory="public", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 3000))
    uvicorn.run(app, host="0.0.0.0", port=port)
