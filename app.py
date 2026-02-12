import streamlit as st
from gradio_client import Client
import time

# ١. دیزاین و ستایلی ڕەنگاوڕەنگ
st.set_page_config(page_title="دیزاینەری زیرەک", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stTitle, .stSubheader { text-align: right; direction: rtl; color: #2D3748; }
    .stButton>button { 
        width: 100%; 
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); 
        color: white; border-radius: 12px; height: 3.5em; font-weight: bold; border: none;
    }
    .stButton>button:hover { opacity: 0.9; transform: scale(1.02); }
    </style>
    """, unsafe_allow_html=True)

st.title("🎨 دروستکەری وێنە و ڤیدیۆی زیرەک")
st.subheader("چی لە خەیاڵتە؟ لێرە بە ئینگلیزی بنووسە")

# ٢. وەرگرتنی وەسف
user_prompt = st.text_area("وەسف (Prompt):", placeholder="Example: A beautiful waterfall in the mountains, 4k...")

# ٣. هەڵبژاردنی جۆر (وێنە یان ڤیدیۆ)
option = st.radio("دەتەوێت چی بۆ دروست بکەم؟", ("وێنەی کوالێتی بەرز (خێرا)", "ڤیدیۆی جوڵاو (کەمێک خاو)"))

if st.button("✨ دەستپێکردن"):
    if user_prompt.strip():
        with st.spinner('🎨 خەریکی ئامادەکردنین...'):
            try:
                if option == "وێنەی کوالێتی بەرز (خێرا)":
                    # مۆدێلی وێنە (زۆر جێگیر و خێرا)
                    client = Client("black-forest-labs/FLUX.1-schnell")
                    result = client.predict(prompt=user_prompt, seed=0, width=1024, height=1024, num_inference_steps=4, api_name="/infer")
                    if result:
                        st.image(result, caption="فەرموو وێنەکەت ئامادەیە", use_container_width=True)
                
                else:
                    # مۆدێلی ڤیدیۆ (کەمێک قەرەباڵغە)
                    client = Client("aliabd/stable-video-diffusion")
                    result = client.predict(user_prompt, 42, api_name="/generate_video")
                    if result:
                        st.video(result)
                        st.success("فەرموو ڤیدیۆکەت ئامادەیە")
                    else:
                        st.error("سێرڤەری ڤیدیۆ لەم کاتەدا وەڵامی نییە، وێنەکە تاقی بکەرەوە.")
                        
            except Exception as e:
                st.error("سێرڤەرەکە کەمێک ماندووە، تکایە دووبارە کلیک بکەرەوە.")
    else:
        st.warning("تکایە سەرەتا وەسفێک بنووسە.")
