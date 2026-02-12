import streamlit as st
from gradio_client import Client
from deep_translator import GoogleTranslator # وەرگێڕی گووگڵ

st.set_page_config(page_title="ڤیدیۆساز", layout="centered")

st.markdown("<style>.stTextArea, .stTitle { text-align: right; direction: rtl; }</style>", unsafe_allow_html=True)
st.title("🎥 دروستکەری ڤیدیۆ بە کوردی")

# وەرگرتنی نووسین بە کوردی
user_input = st.text_area("بە کوردی بنووسە چ ڤیدیۆیەک جەنابت دەوێت:", placeholder="بۆ نموونە: ئەسپێکی سپی لەناو دارستان...")

if st.button("ڤیدیۆکە دروست بکە"):
    if user_input.strip():
        with st.spinner('خەریکی وەرگێڕان و دروستکردنی ڤیدیۆکەین...'):
            try:
                # ١. وەرگێڕانی کوردی بۆ ئینگلیزی
                translated_prompt = GoogleTranslator(source='ku', target='en').translate(user_input)
                st.info(f"وەسفەکە وەرگێڕدرا بۆ: {translated_prompt}")

                # ٢. پەیوەندی بە سێرڤەری ڤیدیۆ
                client = Client("aliabd/stable-video-diffusion")
                result = client.predict(translated_prompt, 42, api_name="/generate_video")

                if result:
                    st.video(result)
                    st.success("فەرموو مامۆستا گیان، ئەمەش ڤیدیۆکە")
            except Exception as e:
                st.error("ببوورە، سێرڤەرەکە کەمێک قەرەباڵغە. دووبارە تاقی بکەرەوە.")
