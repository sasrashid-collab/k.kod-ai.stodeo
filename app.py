import streamlit as st
import os
from gradio_client import Client

# ١. ڕێکخستنی شێوەی لاپەڕەکە
st.set_page_config(page_title="دروستکەری ڤیدیۆ", layout="centered")

# ٢. ستایلی ڕەنگەکان و نووسینی کوردی (ڕاست بۆ چەپ)
st.markdown("""
    <style>
    .stTextArea, .stMarkdown, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background-color: #FF4B4B; color: white; border-radius: 12px; height: 3em; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎥 دروستکەری ڤیدیۆی زیرەک")
st.subheader("وەسفی ڤیدیۆکە بنووسە (بۆ نموونە: پیاوێکی کورد لە قەڵای هەولێر)")

# ٣. شوێنی نووسینی وەسفەکە
user_prompt = st.text_area("چی لە خەیاڵتە؟", placeholder="بۆ نموونە: A horse running in the snow...")

if st.button("دروستکردنی ڤیدیۆ"):
    if user_prompt.strip():
        with st.spinner('خەریکی دروستکردنی ڤیدیۆکەین... تکایە کەمێک چاوەڕێ بکە'):
            try:
                # ٤. پەیوەندیکردن بە مۆدێلەکە
                client = Client("THUDM/CogVideoX-5B-Space")
                
                # ٥. ناردنی زانیارییەکان بەبێ ناوی پارامیتەرەکان بۆ دوورکەوتنەوە لە هەڵەی Seed
                # لێرەدا تەنها زانیارییەکان بە ڕیزبەندی دەنێرین
                result = client.predict(
                    user_prompt + ", cinematic style, 4k", # دەقی ڤیدیۆکە
                    42,                                   # Seed
                    6,                                    # Guidance scale
                    50,                                   # Inference steps
                    api_name="/generate"
                )

                # ٦. وەرگرتنی ئەنجام و نیشاندانی
                if result:
                    # ئەگەر ئەنجامەکە لیست بێت دانەی یەکەمی وەردەگرین
                    video_path = result[0] if isinstance(result, list) else result
                    
                    if os.path.exists(video_path):
                        st.success("ڤیدیۆکە بە سەرکەوتوویی دروستکرا!")
                        st.video(video_path)
                        
                        with open(video_path, "rb") as f:
                            st.download_button("📥 دابەزاندنی ڤیدیۆکە", f, "video.mp4")
                else:
                    st.error("سێرڤەرەکە نەیتوانی ڤیدیۆکە دروست بکات.")
                    
            except Exception as e:
                st.error(f"کێشەیەک ڕوویدا: {str(e)}")
    else:
        st.warning("تکایە سەرەتا وەسفێک بنووسە.")
