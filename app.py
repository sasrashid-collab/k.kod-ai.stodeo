import streamlit as st
import os
from deep_translator import GoogleTranslator

# إعداد الواجهة الكوردية
st.set_page_config(page_title="دروستکەری ڤیدیۆ", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stMarkdown, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background-color: #FF4B4B; color: white; border-radius: 12px; height: 3em; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎥 دروستکەری ڤیدیۆی زیرەک")
st.subheader("وەسفی ڤیدیۆکە بە زمانی کوردی بنووسە")

sorani_input = st.text_area("چی لە خەیاڵتە؟", placeholder="بۆ نموونە: پیاوێکی کورد لە ناو قەڵای هەولێر...")

if st.button("دروستکردنی ڤیدیۆ"):
    if sorani_input.strip():
        with st.spinner('خەریکی وەرگێڕان و دروستکردنی ڤیدیۆکەین... تکایە چاوەڕێ بکە'):
            try:
                from gradio_client import Client
                
                # استخدام المترجم البديل القوي (يدعم السورانية بذكاء)
                # نترك المصدر 'auto' ليتمكن من التعرف على الكوردية تلقائياً
                translated_text = GoogleTranslator(source='auto', target='en').translate(sorani_input)
                
                st.info(f"وەسفی وەرگێڕدراو: {translated_text}")

                # إرسال النص المترجم لمحرك الفيديو
                client = Client("THUDM/CogVideoX-5B-Space")
                result = client.predict(
                    prompt=translated_text + ", cinematic style, 4k",
                    seed=42,
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
                st.error(f"هەڵەیەک ڕوویدا: {str(e)}")
    else:
        st.warning("تکایە وەسفێک بنووسە!")
