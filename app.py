import streamlit as st
import subprocess
import sys
import os

# --- خطوة إجبارية لتثبيت المكتبات لضمان عمل التطبيق ---
def install_requirements():
    try:
        from googletrans import Translator
        from gradio_client import Client
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "googletrans==4.0.0-rc1", "gradio_client"])
        st.rerun()

# تشغيل التثبيت التلقائي
install_requirements()

from googletrans import Translator
from gradio_client import Client

# --- إعداد واجهة التطبيق بالكردية ---
st.set_page_config(page_title="دروستکەری ڤیدیۆ", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stMarkdown, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background-color: #FF4B4B; color: white; border-radius: 12px; height: 3em; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎥 دروستکەری ڤیدیۆی زیرەک")
st.subheader("وەسفی ڤیدیۆکە بە زمانی کوردی بنووسە")

# مدخل النص
sorani_input = st.text_area("چی لە خەیاڵتە؟", placeholder="بۆ نموونە: ئەسپێکی سپی لە کاتی خۆرئاوابوون...")

if st.button("دروستکردنی ڤیدیۆ"):
    if sorani_input.strip():
        with st.spinner('خەریکی وەرگێڕان و دروستکردنی ڤیدیۆکەین... تکایە چاوەڕێ بکە'):
            try:
                # الترجمة والتوليد
                translator = Translator()
                translation = translator.translate(sorani_input, src='ckb', dest='en')
                english_prompt = translation.text + ", cinematic, 4k, detailed"
                
                st.info(f"وەسفی وەرگێڕدراو: {translation.text}")

                client = Client("THUDM/CogVideoX-5B-Space")
                result = client.predict(prompt=english_prompt, seed=42, api_name="/generate")

                if result and os.path.exists(result):
                    st.success("ڤیدیۆکە بە سەرکەوتوویی دروستکرا!")
                    st.video(result)
                    with open(result, "rb") as f:
                        st.download_button("📥 دابەزاندنی ڤیدیۆکە", f, "video.mp4")
                else:
                    st.error("سێرڤەرەکە وەڵامی نەبوو.")
            except Exception as e:
                st.error(f"هەڵەیەک ڕوویدا: {str(e)}")
    else:
        st.warning("تکایە وەسفێک بنووسە!")

