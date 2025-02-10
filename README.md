# AskYourVideo

## About
AskYourVideo is an AI-powered application that lets you interact with video content through natural language questions. Upload a video, get it transcribed, and ask questions about its content using advanced AI models.

## Tech Stack

 Streamlit (Web Interface)

 FFmpeg (Audio processing)

 Qwen2.5-1.5B-Instruct (to answer questions about the text of the video)

 Whisper-small (Speech recognition)

## Installation
Clone the repository:
```bash
git clone https://github.com/MRuslanR/AskYourVideo.git
```
```bash
cd askyourvideo
```

Install system dependencies:
```bash
sudo apt-get install ffmpeg(Ubuntu/Debian example)
```
```bash
brew install ffmpeg (MacOS)
```

Create venv:
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```


Install Python dependencies:
```bash
pip install -r requirements.txt
```

Running the Application:
```bash
streamlit run app.py
```
The application will open in your default browser at http://localhost:8501


# Hugging Face Space : https://huggingface.co/spaces/MRuslanR/AskYourVideo

<img width="638" alt="Снимок экрана 2025-02-10 в 21 04 29" src="https://github.com/user-attachments/assets/d2beed93-5a92-4bbb-8acb-a417bc8c8531" />




