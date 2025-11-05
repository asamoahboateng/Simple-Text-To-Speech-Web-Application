# 🗣️ Text-to-Speech Web App

A simple Flask-based web application that converts text to speech using **gTTS (Google Text-to-Speech)**.  
You can type text into the browser, hit "Speak", and the app will read it aloud.

---

## 🚀 How to Run (with Docker)

### 1️⃣ Build and start the app
```bash
docker-compose up --build
```

### 2️⃣ Open in browser
Go to 👉 http://localhost:5000

### 3️⃣ Stop the app
```bash
docker-compose down
```

## 🧰 Tech Stack
- Python 3.12
- Flask
- gTTS (Google Text-to-Speech)
- Docker + Docker Compose


## 📂 Project Structure
```bash
tts-webapp/
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

### Demo 
https://tts.asamoahboateng.com


## 🗒️ Notes
- Requires an internet connection (gTTS uses Google’s online API).
- Works out of the box with Docker.
- Add text, click Speak, and enjoy natural speech output!


## License