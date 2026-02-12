import streamlit as st
from gradio_client import Client
from googletrans import Translator # وەرگێڕی فەرمی

# ١. ڕێکخستنی شاشە
st.set_page_config(page_title="ڤیدیۆساز بە کوردی", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background-color: #28a745; color: white; border-radius: 10px; height: 3em; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎥 دروستکەری ڤیدیۆ بە زمانی کوردی")
st.subheader("بە کوردی بنووسە، ئێمە دەیکەین بە ڤیدیۆ")

# ٢. وەرگرتنی وەسف بە کوردی
user_ku = st.text_area("چی دروست بکەین؟", placeholder="بۆ نموونە: پڵنگێک لەناو جەنگەڵدا ڕادەکات...")

if st.button("دەستپێکردن"):
    if user_ku.strip():
        with st.spinner('خەریکی وەرگێڕان و دروستکردنی ڤیدیۆکەین...'):
            try:
                # هەنگاوی یەکەم: وەرگێڕان بۆ ئینگلیزی
                translator = Translator()
                translation = translator.translate(user_ku, src='ku', dest='en')
                english_text = translation.text
                
                st.info(f"وەسفەکە وەرگێڕدرا بۆ: {english_text}")

                # هەنگاوی دووەم: ناردنی بۆ سێرڤەری ڤیدیۆ
                client = Client("aliabd/stable-video-diffusion")
                result = client.predict(english_text, 42, api_name="/generate_video")

                if result:
                    st.success("فەرموو مامۆستا گیان، ڤیدیۆکە ئامادەیە:")
                    st.video(result)
                else:
                    st.error("سێرڤەرەکە وەڵامی نییە، دووبارە تاقی بکەرەوە.")
                    
            except Exception as e:
                st.error(f"کێشەیەک ڕوویدا: تکایە دڵنیابە لە ئینتەرنێتەکەت.")
    else:
        st.warning("تکایە وەسفێک بنووسە.")
