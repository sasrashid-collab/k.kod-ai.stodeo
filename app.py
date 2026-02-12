import streamlit as st
import random

# ١. دیزاینی شاشە
st.set_page_config(page_title="وێنەسازی کوردی", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background: #E91E63; color: white; border-radius: 12px; height: 3.5em; font-weight: bold; border: none; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎨 وێنەسازی زیرەک (وەشانی جێگیر)")
st.subheader("بە کوردی بنووسە چیت دەوێت:")

user_ku = st.text_area("چی دروست بکەم؟", placeholder="بۆ نموونە: شارێکی کوردی لە داهاتوودا...")

if st.button("✨ وێنەکە دروست بکە"):
    if user_ku.strip():
        # گۆڕینی وەسفەکە بۆ لینکێکی جیاواز کە بلۆک نابێت
        clean_prompt = user_ku.replace(" ", "+")
        seed = random.randint(0, 999999)
        
        # بەکارهێنانی سێرڤەرێکی تری جیهانی (DummyImage/Robohash یان لایەنی تر)
        # لێرەدا فێڵێکی تر دەکەین بۆ ئەوەی براوزەر بلۆکی نەکات
        image_url = f"https://image.pollinations.ai{clean_prompt}?width=800&height=800&seed={seed}&nologo=true"
        
        with st.spinner('🎨 خەریکی کێشانی وێنەکەین...'):
            # بەکارهێنانی مارکداون بۆ نیشاندانی وێنەکە (براوزەر کەمتر بلۆکی دەکات)
            st.markdown(f'<img src="{image_url}" style="width:100%; border-radius:15px;">', unsafe_allow_html=True)
            
            st.info("📥 بۆ دابەزاندن: پەنجە لەسەر وێنەکە دابگرە و (Download Image) هەڵبژێرە.")
    else:
        st.warning("تکایە سەرەتا شتێک بنووسە.")
