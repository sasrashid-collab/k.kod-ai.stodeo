import streamlit as st
import os

# 1. ڕێکخستنی واژە (UI)
st.set_page_config(page_title="دروستکەری ڤیدیۆ", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stMarkdown, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background-color: #FF4B4B; color: white; border-radius: 12px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎥 دروستکەری ڤیدیۆی زیرەک")
st.subheader("وەسفی ڤیدیۆکە بە کوردی یان ئینگلیزی بنووسە")

# 2. خانة النص (نكتب فيها أي وصف بسيط)
user_prompt = st.text_area("چی لە خەیاڵتە؟", placeholder="Example: A horse in the snow...")

if st.button("دروستکردنی ڤیدیۆ"):
    if user_prompt.strip():
        with st.spinner('خەریکی دروستکردنی ڤیدیۆکەین...'):
            try:
                from gradio_client import Client
                # الاتصال بالمحرك مباشرة بدون مترجم لتجنب الأخطاء
                client = Client("THUDM/CogVideoX-5B-Space")
                
                result = client.predict(
                    prompt=user_prompt + ", cinematic style, 4k",
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
                st.error(f"کێشەیەک ڕوویدا: {str(e)}")
    else:
        st.warning("تکایە وەسفێک بنووسە.")
