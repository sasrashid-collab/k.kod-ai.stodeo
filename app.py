import streamlit as st
from gradio_client import Client
import os

# ١. دیزاینی شاشە
st.set_page_config(page_title="گۆڕینی ڕووخسار", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stTitle, .stSubheader { text-align: right; direction: rtl; color: #4B0082; }
    .stButton>button { 
        width: 100%; 
        background: linear-gradient(45deg, #FF8C00, #FF0000); 
        color: white; border-radius: 12px; height: 3.5em; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎭 گۆڕینی تەمەن بە زیرەکی دەستکرد")
st.subheader("وێنەکەت لێرە دابنێ و تەمەنت بگۆڕە")

# ٢. بەشی بارکردنی وێنە (Upload)
uploaded_file = st.file_uploader("وێنەکەت لێرە هەڵبژێرە...", type=["jpg", "jpeg", "png"])

# ٣. وەسفی گۆڕانکارییەکە
target_age = st.radio("دەتەوێت چۆن دەربکەویت؟", ("ببم بە پیر (Old man)", "ببم بە گەنج (Young person)"))

if st.button("✨ جادوو بکە"):
    if uploaded_file is not None:
        with st.spinner('🎨 خەریکی گۆڕینی ڕووخسارین...'):
            try:
                # پاشکەوتکردنی وێنە بارکراوەکە بە کاتی
                with open("input.png", "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                # بەکارهێنانی مۆدێلی InstructPix2Pix کە وێنە دەگۆڕێت
                client = Client("timbrooks/instruct-pix2pix")
                result = client.predict(
                    image="input.png",
                    prompt=f"Make this person look like a {target_age}",
                    api_name="/predict"
                )

                if result:
                    st.success("فەرموو مامۆستا گیان، ئەمەش ئەنجامەکە:")
                    st.image(result, use_container_width=True)
                else:
                    st.error("سێرڤەرەکە وەڵامی نەبوو، دووبارە تاقی بکەرەوە.")
            except Exception as e:
                st.error("سێرڤەرەکە کەمێک قەرەباڵغە، تکایە کەمێکی تر کلیک بکەرەوە.")
    else:
        st.warning("تکایە سەرەتا وێنەیەک هەڵبژێرە.")
