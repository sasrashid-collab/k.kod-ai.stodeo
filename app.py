import streamlit as st
import requests
import random

# ١. دیزاینی شاشە
st.set_page_config(page_title="وێنەساز", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background: #2ecc71; color: white; border-radius: 12px; height: 3.5em; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎨 وێنەسازی خێرا بە زمانی کوردی")
st.subheader("بە کوردی بنووسە چیت دەوێت:")

# ٢. وەرگرتنی نووسینی کوردی
user_ku = st.text_area("چی دروست بکەم؟", placeholder="بۆ نموونە: پڵنگێک لەناو بەفردا...")

if st.button("✨ ئێستا وێنەکە بکێشە"):
    if user_ku.strip():
        # دروستکردنی لوتکەی لینکەکە
        clean_prompt = user_ku.replace(" ", "%20")
        seed = random.randint(0, 999999)
        image_url = f"https://pollinations.ai{clean_prompt}?width=1024&height=1024&seed={seed}&enhance=true"
        
        with st.spinner('🎨 چاوەڕێ بکە مامۆستا گیان...'):
            try:
                # نیشاندانی وێنەکە
                st.image(image_url, caption="ئەمەش وێنەکە بەبێ Error!", use_container_width=True)
                
                # ٣. چارەسەری کێشەی دابەزاندن: وەرگرتنی داتا و دروستکردنی دوگمەی دابەزاندن
                img_data = requests.get(image_url).content
                st.download_button(
                    label="📥 دابەزاندنی وێنەکە بۆ ناو مۆبایلەکەت",
                    data=img_data,
                    file_name="kurdistan_ai_image.jpg",
                    mime="image/jpeg"
                )
            except:
                st.error("کێشەیەک لە دابەزاندنی فایلەکە هەبوو، بەڵام وێنەکە لێرە دیارە.")
    else:
        st.warning("تکایە سەرەتا شتێک بنووسە.")
