import streamlit as st
import os

# إعداد الواجهة
st.set_page_config(page_title="دروستکەری ڤیدیۆ", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stMarkdown, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background-color: #FF4B4B; color: white; border-radius: 12px; height: 3em; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎥 دروستکەری ڤیدیۆی زیرەک")
st.subheader("وەسفی ڤیدیۆکە بنووسە (بۆ نموونە: Kurdish man, Erbil castle)")

user_prompt = st.text_area("چی لە خەیاڵتە؟", placeholder="Example: A horse in the snow...")

if st.button("دروستکردنی ڤیدیۆ"):
    if user_prompt.strip():
        with st.spinner('خەریکی دروستکردنی ڤیدیۆکەین... تکایە چاوەڕێ بکە'):
            try:
                from gradio_client import Client
                # الاتصال بالمحرك العالمي (النسخة المحدثة)
                client = Client("THUDM/CogVideoX-5B-Space")
                
                # إرسال الأمر الصافي للمحرك بدون پارامیتەری seed
                result = client.predict(
                    prompt=user_prompt + ", cinematic style, 4k",
                    api_name="/generate"
                )

                if result and os.path.exists(result):
                    st.success("ڤیدیۆکە بە سەرکەوتوویی دروستکرا!")
                    st.video(result)
                    with open(result, "rb") as f:
                        st.download_button("📥 دابەزاندنی ڤیدیۆکە", f, "video.mp4")
                else:
                    st.error("سێرڤەرەکە وەڵامی نەبوو.")
            except Exception as e:
                st.error(f"کێشەیەک ڕوویدا: {str(e)}")
    else:
        st.warning("تکایە وەسفێک بنووسە.")
