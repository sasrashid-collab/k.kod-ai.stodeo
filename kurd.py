import streamlit as st
import os

# 1. إعداد الواجهة الكوردية
st.set_page_config(page_title="دروستکەری ڤیدیۆ", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stMarkdown, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background-color: #FF4B4B; color: white; border-radius: 12px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎥 دروستکەری ڤیدیۆی زیرەک")
st.subheader("وەسفی ڤیدیۆکە بنووسە")

# 2. خانة إدخال النص (سنتعامل معه كأمر مباشر للمحرك)
sorani_input = st.text_area("چی لە خەیاڵتە؟", placeholder="بۆ نموونە: Kurdish man, mountains, cinematic...")

if st.button("دروستکردنی ڤیدیۆ"):
    if sorani_input.strip():
        with st.spinner('خەریکی دروستکردنی ڤیدیۆکەین...'):
            try:
                from gradio_client import Client
                client = Client("THUDM/CogVideoX-5B-Space")
                
                # نرسل النص مباشرة لتجنب أخطاء الترجمة
                result = client.predict(prompt=sorani_input + ", 4k, cinematic", seed=42, api_name="/generate")

                if result and os.path.exists(result):
                    st.success("ڤیدیۆکە بە سەرکەوتوویی دروستکرا!")
                    st.video(result)
                    with open(result, "rb") as f:
                        st.download_button("📥 دابەزاندنی ڤیدیۆکە", f, "video.mp4")
                else:
                    st.error("سێرڤەرەکە وەڵامی نەبوو.")
            except Exception as e:
                st.error(f"کێشەیەک ڕوویدا: {str(e)}")
