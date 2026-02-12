import streamlit as st
import os
from gradio_client import Client

# ١. ڕێکخستنی لاپەڕە
st.set_page_config(page_title="دروستکەری ڤیدیۆ", layout="centered")

# ٢. ستایلی کوردی
st.markdown("""
    <style>
    .stTextArea, .stMarkdown, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background-color: #008CBA; color: white; border-radius: 10px; height: 3em; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎥 دروستکەری ڤیدیۆی خێرا")
st.subheader("وەسفی ڤیدیۆکە بە ئینگلیزی بنووسە:")

user_prompt = st.text_area("چی دروست بکەم؟", placeholder="بۆ نموونە: A beautiful sunset over the mountains...")

if st.button("دەستپێکردنی دروستکردن"):
    if user_prompt.strip():
        with st.spinner('تکایە کەمێک چاوەڕێ بکە، خەریکە دروستی دەکەین...'):
            try:
                # بەکارهێنانی مۆدێلێکی جێگیرتر و خێراتر
                client = Client("aliabd/stable-video-diffusion")
                
                # ناردنی وەسفەکە بۆ سێرڤەر
                result = client.predict(
                    user_prompt, # Prompt
                    42,          # Seed
                    api_name="/generate_video"
                )

                if result:
                    # نیشاندانی ڤیدیۆکە
                    st.success("تەواو بوو! فەرموو ڤیدیۆکە ئامادەیە:")
                    st.video(result)
                    
                    with open(result, "rb") as f:
                        st.download_button("📥 دابەزاندنی ڤیدیۆکە", f, "video.mp4")
                else:
                    st.error("ببوورە، سێرڤەرەکە لەم کاتەدا وەڵامی نییە. کەمێکی تر تاقی بکەرەوە.")
                    
            except Exception as e:
                st.error("کێشەیەک لە پەیوەندی سێرڤەر ڕوویدا. تکایە دووبارە کلیک بکەرەوە.")
    else:
        st.warning("تکایە سەرەتا وەسفێک بنووسە.")
