🎥 Multilingual Meeting Assistant

A smart meeting assistant that extracts audio from video files, transcribes speech using Whisper, translates it into multiple languages, and generates concise summaries. Perfect for multilingual teams, online meetings, and content analysis.

📝 Features

Upload video files (mp4, mkv, avi, mov).

Automatic audio extraction from video.

Speech transcription using Whisper.

Translation to multiple languages (ar, en, fr, de, es) using Helsinki-NLP.

Text summarization using TextRank algorithm.

User-friendly Streamlit interface.

🚀 Installation

Clone the repository:

git clone https://github.com/YourUsername/Multilingual-Meeting-Assistant.git
cd Multilingual-Meeting-Assistant


Create a virtual environment and activate it:

python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Mac/Linux
source .venv/bin/activate


Install dependencies:

pip install -r requirements.txt

🎯 Usage

Run the Streamlit app:

streamlit run app1.py


Upload your video file.

Wait for audio extraction and transcription.

Optionally, select a language to translate the transcript.

View the summarized text directly in the app.

🛠 Tech Stack

Python

Streamlit for web interface

Whisper for speech-to-text

Transformers (Helsinki-NLP) for translation

Sumy for text summarization

📂 Folder Structure
├─ assets/          # Extracted audio files
├─ app1.py          # Main Streamlit app
├─ requirements.txt # Python dependencies
└─ README.md        # Project documentation

⚡ Notes

Whisper uses FP32 on CPU (slightly slower than GPU).

Translations are optional and depend on Helsinki-NLP models.
