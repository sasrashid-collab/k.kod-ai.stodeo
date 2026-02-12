import streamlit as st
import random

st.set_page_config(page_title="وێنەسازی کوردی", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background: #E91E63; color: white; border-radius: 12px; height: 3.5em; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎨 وێنەسازی کوردی (وەشانی جێگیر)")
st.subheader("بە کوردی بنووسە چیت دەوێت:")

user_ku = st.text_area("وەسفی وێنە:", placeholder="بۆ نموونە: قەڵای هەولێر لە داهاتوودا...")

if st.button("✨ ئێستا وێنەکە دروست بکە"):
    if user_ku.strip():
        clean_prompt = user_ku.replace(" ", ",")
        seed = random.randint(0, 999999)
        
        # گۆڕینی سێرڤەر بۆ دانەیەکی جیاواز کە بلۆک ناکرێت
        image_url = f"https://loremflickr.com{clean_prompt}"
        
        with st.spinner('🎨 خەریکی کێشانین...'):
            # نیشاندانی وێنەکە
            st.image(image_url, use_container_width=True)
            
            st.info("📥 بۆ دابەزاندن: کلیکی ڕاست لەسەر وێنەکە بکە و Save Image As دابگرە.")
    else:
        st.warning("تکایە سەرەتا شتێک بنووسە.")
