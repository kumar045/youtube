import streamlit as st
from pytube import YouTube

def fetch_and_save_transcript(url, language_code='en'):
    try:
        yt = YouTube(url)
        transcript = yt.captions[language_code]
        transcript_str = transcript.generate_srt_captions()
        
        with open("transcript.srt", "w") as f:
            f.write(transcript_str)
        
        return "Transcript saved as transcript.srt"
    except Exception as e:
        return str(e)

# Streamlit App
st.title("YouTube Transcript Downloader")

url = st.text_input("Enter YouTube Video URL:", "")
language_code = st.text_input("Enter language code (default is 'en'):", "en")

if st.button("Download Transcript"):
    result = fetch_and_save_transcript(url, language_code)
    st.write(result)
  
