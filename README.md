# Hej – Real-Time Language Learning App

A minimal web app demonstrating real-time, speech-to-speech language practice using WebRTC and the OpenAI Realtime API (GPT-4o).

## Features

- Live voice conversation with an AI tutor
- Real-time transcription, VAD turn detection, and audio playback
- Simple UI: one button to start
- Logs events (transcripts, model messages) in the browser console

## Prerequisites

- Node.js (v18+) or Python (3.8+)
- npm or pip
- A valid OpenAI API key

## Setup & Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/MasMedIm/Hej.git
   cd Hej
   ```
2. **Create a `.env` file** in the project root (both backends use this):
   ```env
   OPENAI_API_KEY=sk-…          # your secret key
   MODEL=gpt-4o-realtime-preview-2024-12-17
   VOICE=verse
   ```

### Node.js backend

3. **Fix npm cache permissions** (if you see EACCES errors):
   ```bash
   sudo chown -R $(id -u):$(id -g) ~/.npm
   ```
4. **Install & start Node server**
   ```bash
   npm install
   npm start
   ```
5. **Open the app** in your browser: http://localhost:3000

### Python (FastAPI) backend

3. **Install Python deps**
   ```bash
   pip install -r requirements.txt
   ```
4. **Start FastAPI server**
   ```bash
   uvicorn main:app --reload --port 3000
   ```
5. **Open the app** in your browser: http://localhost:3000

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
