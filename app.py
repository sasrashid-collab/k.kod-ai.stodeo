import streamlit as st
from gradio_client import Client
import time

# ١. ڕێکخستنی لاپەڕە
st.set_page_config(page_title="ڤیدیۆساز", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stTitle { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background-color: #007bff; color: white; border-radius: 10px; height: 3em; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎥 دروستکەری ڤیدیۆی بێبەرامبەر")
st.info("ئەگەر سێرڤەرەکە قەرەباڵغ بوو، ئێمە خۆمان دووبارە تاقی دەکەینەوە...")

user_input = st.text_area("چی دروست بکەم؟ (بە ئینگلیزی):", placeholder="Example: A fast car in the mountain...")

if st.button("دروستکردنی ڤیدیۆ"):
    if user_input.strip():
        with st.spinner('خەریکی دروستکردنین... تکایە کەمێک ئارام بگرە'):
            success = False
            attempts = 0
            while not success and attempts < 3: # ٣ جار تاقی دەکاتەوە ئەگەر هەڵەی دا
                try:
                    # بەکارهێنانی سێرڤەرێکی جێگیرتر بۆ ڤیدیۆی کورت
                    client = Client("aliabd/stable-video-diffusion")
                    result = client.predict(user_input, 42, api_name="/generate_video")
                    
                    if result:
                        st.success("فەرموو مامۆستا گیان، ڤیدیۆکە ئامادەیە:")
                        st.video(result)
                        success = True
                except Exception:
                    attempts += 1
                    st.warning(f"هەوڵی ژمارە {attempts}: سێرڤەر قەرەباڵغە، کەمێکی تر چاوەڕێ بکە...")
                    time.sleep(5) # ٥ چرکە چاوەڕێ دەکات و دووبارە دەست پێ دەکاتەوە
            
            if not success:
                st.error("ببوورە مامۆستا، سێرڤەرەکان زۆر قەرەباڵغن. تکایە چەند خولەکێکی تر تاقی بکەرەوە.")
    else:
        st.warning("تکایە وەسفەکە بنووسە.")
