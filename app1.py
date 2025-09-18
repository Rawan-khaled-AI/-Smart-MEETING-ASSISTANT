import os
import tempfile
import subprocess
import streamlit as st
import whisper
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

os.makedirs("assets", exist_ok=True)

@st.cache_resource
def load_whisper_model():
    return whisper.load_model("base")  

def extract_audio(video_path, output_path="assets/audio.wav"):
    command = [
        "ffmpeg",
        "-y",  
        "-i", video_path,
        "-vn", 
        "-acodec", "pcm_s16le",  
        "-ar", "16000",  
        "-ac", "1",  
        output_path
    ]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return output_path

def transcribe_audio(audio_path, model):
    result = model.transcribe(audio_path)
    return result["text"]

def translate_text(text, target_lang="ar"):
    lang_map = {
        "ar": "Helsinki-NLP/opus-mt-en-ar",
        "en": "Helsinki-NLP/opus-mt-ar-en",
        "fr": "Helsinki-NLP/opus-mt-en-fr",
    }
    if target_lang not in lang_map:
        return text

    model_name = lang_map[target_lang]
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    translated_tokens = model.generate(**inputs)
    return tokenizer.decode(translated_tokens[0], skip_special_tokens=True)


def summarize_text(text, sentence_count=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return " ".join(str(s) for s in summary)


st.title("🎥 Smart Meeting Assistant")

uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mkv", "avi", "mov"])

if uploaded_file:
    st.video(uploaded_file)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
        tmp.write(uploaded_file.read())
        video_path = tmp.name

    audio_path = extract_audio(video_path)
    st.audio(audio_path)
    model = load_whisper_model()
    with st.spinner("Transcribing..."):
        transcript = transcribe_audio(audio_path, model)
    st.subheader("📝 Transcript")
    st.write(transcript)

    target_lang = st.selectbox("Translate to", ["None", "ar", "en", "fr"])
    translated_text = transcript
    if target_lang != "None":
        with st.spinner("Translating..."):
            translated_text = translate_text(transcript, target_lang)
        st.subheader("🌍 Translated Text")
        st.write(translated_text)



