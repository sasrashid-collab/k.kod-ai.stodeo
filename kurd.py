import streamlit as st
import os

# 1. إعداد الواجهة
st.set_page_config(page_title="دروستکەری ڤیدیۆ", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stMarkdown, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background-color: #FF4B4B; color: white; border-radius: 12px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎥 دروستکەری ڤیدیۆی زیرەک")
st.subheader("وەسفی ڤیدیۆکە بە کوردی بنووسە")

# 2. القاموس الذكي المدمج (لا يحتاج إنترنت للترجمة)
dictionary = {
    "ئەسپ": "horse", "پیاو": "man", "کوردستان": "Kurdistan", 
    "قەڵا": "castle", "هەولێر": "Erbil", "چیا": "mountains",
    "بەفر": "snow", "دارستان": "forest", "شار": "city",
    "کچ": "girl", "ژن": "woman", "منداڵ": "child", "خۆر": "sun"
}

sorani_input = st.text_area("چی لە خەیاڵتە؟ (بۆ نموونە: ئەسپ، قەڵا، چیا...)", placeholder="وەسفەکەت بنووسە...")

if st.button("دروستکردنی ڤیدیۆ"):
    if sorani_input.strip():
        with st.spinner('خەریکی دروستکردنی ڤیدیۆکەین...'):
            try:
                from gradio_client import Client
                
                # تحويل الكلمات الكوردية يدوياً من القاموس
                words = sorani_input.split()
                translated_words = [dictionary.get(w, w) for w in words]
                final_prompt = " ".join(translated_words) + ", cinematic style, 4k"
                
                st.info(f"وەسفی وەرگێڕدراو: {final_prompt}")

                client = Client("THUDM/CogVideoX-5B-Space")
                result = client.predict(prompt=final_prompt, seed=42, api_name="/generate")

                if result and os.path.exists(result):
                    st.success("ڤیدیۆکە بە سەرکەوتوویی دروستکرا!")
                    st.video(result)
                    with open(result, "rb") as f:
                        st.download_button("📥 دابەزاندنی ڤیدیۆکە", f, "video.mp4")
                else:
                    st.error("سێرڤەرەکە وەڵامی نەبوو.")
            except Exception as e:
                st.error(f"کێشەیەک ڕوویدا: {str(e)}")
