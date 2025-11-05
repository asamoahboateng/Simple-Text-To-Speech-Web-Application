# Use lightweight Python base image
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

# Install system dependencies for gTTS + ffmpeg
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy dependency file and install Python libs
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

EXPOSE 5000

# Run Flask app
CMD ["flask", "--app", "app", "run", "--host=0.0.0.0", "--port=5000"]
