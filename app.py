import streamlit as st
import os
from gradio_client import Client

# ڕێکخستنی لاپەڕە
st.set_page_config(page_title="دروستکەری ڤیدیۆ", layout="centered")

# ستایلی کوردی و ڕاست بۆ چەپ
st.markdown("""
    <style>
    .stTextArea, .stMarkdown, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background-color: #FF4B4B; color: white; border-radius: 12px; height: 3em; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎥 دروستکەری ڤیدیۆی زیرەک")
st.subheader("وەسفی ڤیدیۆکە بنووسە (بۆ نموونە: Kurdish man, Erbil castle)")

user_prompt = st.text_area("چی لە خەیاڵتە؟", placeholder="بۆ نموونە: ئەسپێک لەناو بەفردا...")

if st.button("دروستکردنی ڤیدیۆ"):
    if user_prompt.strip():
        with st.spinner('خەریکی دروستکردنی ڤیدیۆکەین... تکایە چاوەڕێ بکە'):
            try:
                # پەیوەندیکردن بە سێرڤەری مۆدێلەکە
                client = Client("THUDM/CogVideoX-5B-Space")
                
                # ناردنی داواکاری بە پارامیتەرە دروستەکان
                result = client.predict(
                    prompt=user_prompt + ", cinematic style, 4k",
                    seed=42,
                    guidance_scale=6,
                    num_inference_steps=50,
                    api_name="/generate"
                )

                # دڵنیابوونەوە لەوەی ئەنجامەکە ڕێڕەوی فایلە (Path)
                video_path = result[0] if isinstance(result, list) else result

                if video_path and os.path.exists(video_path):
                    st.success("ڤیدیۆکە بە سەرکەوتوویی دروستکرا!")
                    st.video(video_path)
                    
                    with open(video_path, "rb") as f:
                        st.download_button("📥 دابەزاندنی ڤیدیۆکە", f, "video.mp4")
                else:
                    st.error("سێرڤەرەکە وەڵامی نەبوو یان فایلی ڤیدیۆکە دروست نەبوو.")
                    
            except Exception as e:
                st.error(f"کێشەیەک ڕوویدا: {str(e)}")
    else:
        st.warning("تکایە وەسفێک بنووسە.")
