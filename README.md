# 🎥 Multilingual Meeting Assistant

A smart meeting assistant that extracts audio from video files, transcribes speech using **Whisper**, translates it into multiple languages, and generates concise summaries. Perfect for multilingual teams, online meetings, and content analysis.

---

## 📝 Features

- Upload video files (`mp4`, `mkv`, `avi`, `mov`).  
- Automatic audio extraction from video.  
- Speech transcription using **Whisper**.  
- Translation to multiple languages (`ar`, `en`, `fr`, `de`, `es`) using **Helsinki-NLP**.  
- Text summarization using **TextRank** algorithm.  
- User-friendly **Streamlit** interface.

---

## 🚀 Installation

1. Clone the repository:  
```bash
git clone https://github.com/YourUsername/Multilingual-Meeting-Assistant.git
cd Multilingual-Meeting-Assistant
```

2. Create a virtual environment and activate it:  
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Mac/Linux
source .venv/bin/activate
```

3. Install dependencies:  
```bash
pip install -r requirements.txt
```

---

## 🎯 Usage

Run the Streamlit app:  
```bash
streamlit run app1.py
```

1. Upload your video file.  
2. Wait for audio extraction and transcription.  
3. Optionally, select a language to translate the transcript.  
4. View the summarized text directly in the app.  

---

## 🛠 Tech Stack

- **Python**  
- **Streamlit** for web interface  
- **Whisper** for speech-to-text  
- **Transformers (Helsinki-NLP)** for translation  
- **Sumy** for text summarization  

---

## 📂 Folder Structure

```
├─ assets/          # Extracted audio files
├─ app1.py          # Main Streamlit app
├─ requirements.txt # Python dependencies
└─ README.md        # Project documentation
```

---

## ⚡ Notes

- Whisper uses FP32 on CPU (slightly slower than GPU).  
- Translations are optional and depend on Helsinki-NLP models.  
