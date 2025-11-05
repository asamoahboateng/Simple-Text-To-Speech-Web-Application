from flask import Flask, request, send_file, render_template
from gtts import gTTS
import io
import logging
import os

app = Flask(__name__)

# Create logs directory
os.makedirs("logs", exist_ok=True)

# Logging setup
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/speak", methods=["POST"])
def speak():
    data = request.get_json()
    text = data.get("text", "").strip()

    if not text:
        logging.warning("Empty text received for speech synthesis.")
        return {"error": "No text provided"}, 400

    try:
        # Generate audio in-memory
        mp3_fp = io.BytesIO()
        tts = gTTS(text)
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)

        logging.info(f"Generated speech for text: {text[:50]}...")

        # Return audio as response
        return send_file(
            mp3_fp,
            mimetype="audio/mpeg",
            as_attachment=False,
            download_name="speech.mp3"
        )
    except Exception as e:
        logging.error(f"Error generating TTS: {e}")
        return {"error": str(e)}, 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
