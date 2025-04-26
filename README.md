# Hej – Real-Time Language Learning App
![Hej presentation](repo_assets/presentation.png)
Try the live demo at [https://tryhej.com](https://tryhej.com)

## Features

- Live voice conversation with an AI tutor
- Real-time transcription, VAD turn detection, and audio playback
- Simple UI: one button to start
- Logs events (transcripts, model messages) in the browser console

## Prerequisites

- Python 3.8+
- pip
- A valid OpenAI API key

## Setup & Run
> Or skip setup and test instantly at [https://tryhej.com](https://tryhej.com)
1. **Clone the repo**
   ```bash
   git clone https://github.com/MasMedIm/Hej.git
   cd Hej
   ```
2. **Create a `.env` file** in the project root:
   ```env
   OPENAI_API_KEY=sk-…          # your secret key
   MODEL=gpt-4o-realtime-preview-2024-12-17
   VOICE=verse
   ```
3. **Install Python deps**
   ```bash
   pip install -r requirements.txt
   ```
4. **Start FastAPI server**
   ```bash
   uvicorn main:app --reload --port 3000
   ```
5. **Open in browser**: http://localhost:3000

## Project Structure

- `server.js` – Express server that mints ephemeral keys via `/session`
- `public/index.html` – WebRTC client: captures mic, exchanges SDP, plays AI audio, logs events
- `.env` – environment variables
- `package.json` – scripts & dependencies

## Extending this Demo

- Replace plain HTML/JS with a frontend framework (React/Vue/Angular)
- Add UI for live transcript display and grammar hints
- Implement function-calling for dynamic exercises or vocabulary quizzes
- Use partner SDKs (LiveKit, Twilio, Agora) for production-grade media

## License

MIT
