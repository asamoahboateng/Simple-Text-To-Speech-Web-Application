from flask import Flask, render_template, request, send_file
from gtts import gTTS
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    audio_data = None

    if request.method == 'POST':
        text = request.form.get('text')
        if text.strip():
            # Convert text to speech
            tts = gTTS(text=text, lang='en')
            mp3_fp = io.BytesIO()
            tts.write_to_fp(mp3_fp)
            mp3_fp.seek(0)
            return send_file(
                mp3_fp,
                mimetype="audio/mpeg",
                as_attachment=False,
                download_name="speech.mp3"
            )
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
