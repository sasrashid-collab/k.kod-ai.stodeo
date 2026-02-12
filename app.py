import streamlit as st
import random

# ١. دیزاینی شاشە
st.set_page_config(page_title="وێنەسازی کوردی", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background: #2ecc71; color: white; border-radius: 12px; height: 3.5em; font-weight: bold; border: none; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎨 وێنەسازی خێرا بە زمانی کوردی")
st.subheader("بە کوردی بنووسە چیت دەوێت:")

user_ku = st.text_area("چی دروست بکەم؟", placeholder="بۆ نموونە: شارێکی کوردی لە داهاتوودا...")

if st.button("✨ ئێستا وێنەکە بکێشە"):
    if user_ku.strip():
        # دروستکردنی لوتکەی لینکەکە لە ڕێگەی MagicStudio (ئەمە بلۆک نابێت)
        clean_prompt = user_ku.replace(" ", "%20")
        seed = random.randint(0, 999999)
        # بەکارهێنانی سێرڤەری وێنەی جێگیر کە براوزەر ڕێگری لێ ناکات
        image_url = f"https://image.pollinations.ai{clean_prompt}?width=1024&height=1024&seed={seed}&nologo=true"
        
        with st.spinner('🎨 چاوەڕێ بکە مامۆستا گیان...'):
            # نیشاندانی وێنەکە
            st.image(image_url, use_container_width=True)
            
            # ڕێنمایی بۆ پاشکەوتکردن
            st.info("📥 بۆ دابەزاندن: ئەگەر بە مۆبایلیت پەنجە لەسەر وێنەکە دابگرە و (Download Image) دابگرە.")
            st.markdown(f"[🔗 کردنەوەی وێنەکە لە پەڕەیەکی نوێ]({image_url})")
    else:
        st.warning("تکایە سەرەتا شتێک بنووسە.")
