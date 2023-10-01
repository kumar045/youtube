import streamlit as st
from pytube import YouTube
import tempfile

def fetch_and_save_transcript(url, language_code='en'):
    try:
        yt = YouTube(url)
        transcript = yt.captions[language_code]
        transcript_str = transcript.generate_srt_captions()
        
        tfile = tempfile.NamedTemporaryFile(delete=False) 
        tfile.write(transcript_str.encode('utf-8'))
        
        return tfile.name, "Transcript fetched successfully."
    except Exception as e:
        return None, str(e)

# Streamlit App
st.title("YouTube Transcript Downloader")

url = st.text_input("Enter YouTube Video URL:", "")
language_code = st.text_input("Enter language code (default is 'en'):", "en")

if st.button("Download Transcript"):
    tmp_file, result = fetch_and_save_transcript(url, language_code)
    if tmp_file:
        st.write(result)
        st.download_button("Download Transcript", tmp_file, file_name="transcript.srt", mime="text/srt")
    else:
        st.write(f"Error: {result}")
        
