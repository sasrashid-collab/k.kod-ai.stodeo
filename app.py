import streamlit as st
from gradio_client import Client

# ١. ڕێکخستنی لاپەڕە
st.set_page_config(page_title="ڤیدیۆساز", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background-color: #E91E63; color: white; border-radius: 10px; height: 3em; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎥 دروستکەری ڤیدیۆی خێرا")
st.subheader("وەسفەکە لێرە بنووسە:")

# وەرگرتنی نووسین (ئەگەر بە کوردی بێت یان ئینگلیزی، مۆدێلە سوکەکە هەوڵ دەدات تێبگات)
user_prompt = st.text_area("چی دروست بکەین؟", placeholder="بۆ نموونە: A horse running...")

if st.button("دروستکردنی ڤیدیۆ"):
    if user_prompt.strip():
        with st.spinner('خەریکی دروستکردنین... تکایە چاوەڕێ بکە'):
            try:
                # بەکارهێنانی مۆدێلێکی زۆر خێرا (Zero-GPU)
                client = Client("fffiloni/stable-video-diffusion-img2vid")
                
                # ناردنی وەسفەکە بۆ سێرڤەرێکی جیاواز
                result = client.predict(
                    user_prompt, # prompt
                    42,          # seed
                    api_name="/generate_video"
                )

                if result:
                    st.success("فەرموو مامۆستا گیان، ڤیدیۆکە ئامادەیە:")
                    st.video(result)
                else:
                    st.error("سێرڤەرەکە لەم ساتەدا زۆر قەرەباڵغە، کەمێکی تر تاقی بکەرەوە.")
            except Exception as e:
                st.error("سێرڤەرەکە تووشی وەستان بووە بەهۆی زۆری داواکاری. دووبارە کلیک بکەرەوە.")
    else:
        st.warning("تکایە سەرەتا وەسفێک بنووسە.")
