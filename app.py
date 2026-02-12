import streamlit as st
from gradio_client import Client
import os

# ١. ڕێکخستنی شاشە
st.set_page_config(page_title="ڤیدیۆساز", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stTitle { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background-color: #4CAF50; color: white; border-radius: 10px; height: 3em; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎥 دروستکەری ڤیدیۆی خێرا")
st.info("تێبینی: تکایە وەسفەکە بە ئینگلیزی بنووسە بۆ ئەوەی سێرڤەرەکە کار بکات")

user_input = st.text_area("چی دروست بکەم؟", placeholder="Example: A cat running in the park...")

if st.button("دروستکردنی ڤیدیۆ"):
    if user_input.strip():
        with st.spinner('خەریکی دروستکردنین...'):
            try:
                # پەیوەندی بە مۆدێلی نوێ
                client = Client("aliabd/stable-video-diffusion")
                
                # ناردنی پارامیتەرەکان بەو شێوەیەی مۆدێلە نوێیەکە دەیەوێت
                result = client.predict(
                    user_input, # prompt
                    42,         # seed
                    api_name="/generate_video"
                )

                if result:
                    st.success("فەرموو مامۆستا گیان:")
                    st.video(result)
                else:
                    st.error("سێرڤەرەکە وەڵامی نەبوو.")
            except Exception as e:
                st.error(f"کێشەیەک ڕوویدا: {str(e)}")
    else:
        st.warning("تکایە وەسفێک بنووسە.")
