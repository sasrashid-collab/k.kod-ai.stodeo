import streamlit as st
from gradio_client import Client
from deep_translator import GoogleTranslator

# ڕێکخستنی شاشە
st.set_page_config(page_title="ڤیدیۆساز", layout="centered")

st.markdown("<style>.stTextArea, .stTitle { text-align: right; direction: rtl; }</style>", unsafe_allow_html=True)
st.title("🎥 دروستکەری ڤیدیۆ بە کوردی")

# وەرگرتنی نووسین بە کوردی
user_ku = st.text_area("وەسفی ڤیدیۆکە بە کوردی بنووسە:", placeholder="بۆ نموونە: ئەسپێک لەناو بەفردا...")

if st.button("ڤیدیۆکە دروست بکە"):
    if user_ku.strip():
        with st.spinner('خەریکی وەرگێڕان و دروستکردنی ڤیدیۆکەین...'):
            try:
                # ١. وەرگێڕان بە شێوازێکی جێگیر (بۆ دوورکەوتنەوە لە AttributeError)
                english_text = GoogleTranslator(source='ku', target='en').translate(user_ku)
                st.info(f"وەسفەکە وەرگێڕدرا بۆ: {english_text}")

                # ٢. پەیوەندی بە سێرڤەری ڤیدیۆ
                client = Client("aliabd/stable-video-diffusion")
                result = client.predict(english_text, 42, api_name="/generate_video")

                if result:
                    st.success("فەرموو مامۆستا گیان، ئەمەش ڤیدیۆکە:")
                    st.video(result)
                else:
                    st.error("سێرڤەرەکە کەمێک قەرەباڵغە، کەمێکی تر تاقی بکەرەوە.")
            except Exception as e:
                st.error("کێشەیەک لە وەرگێڕان یان سێرڤەرەکە ڕوویدا.")
    else:
        st.warning("تکایە سەرەتا وەسفێک بنووسە.")
