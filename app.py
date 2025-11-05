import logging
import os

# Create logs directory if not exists
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

from flask import Flask, request, render_template, jsonify
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text", "")
        logging.info(f"Received text: {text}")
        # You can call your gTTS or TTS function here
        return jsonify({"status": "ok", "text": text})
    return render_template("index.html")

if __name__ == "__main__":
    logging.info("Starting Flask TTS app...")
    app.run(host="0.0.0.0", port=5000)
