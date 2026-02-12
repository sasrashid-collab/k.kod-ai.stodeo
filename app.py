import streamlit as st
import random

# ١. دیزاینی شاشە بۆ گەنجی کورد
st.set_page_config(page_title="وێنەساز", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background: #2ecc71; color: white; border-radius: 12px; height: 3.5em; font-weight: bold; border: none; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎨 وێنەسازی خێرا بە زمانی کوردی")
st.subheader("بە کوردی بنووسە چیت دەوێت:")

# ٢. وەرگرتنی وەسف بە کوردی
user_ku = st.text_area("چی دروست بکەم؟", placeholder="بۆ نموونە: ئەسپێکی سپی لەناو دارستان...")

if st.button("✨ ئێستا وێنەکە بکێشە"):
    if user_ku.strip():
        # فێڵێکی زیرەکانە: ناردنی دەقە کوردییەکە بۆ سێرڤەری وێنە کە خۆی وەرگێڕانی تێدایە
        clean_prompt = user_ku.replace(" ", "%20")
        seed = random.randint(0, 999999)
        
        # ئەم لینکە هەمیشە کار دەکات و زمانی کوردییش دەخوێنێتەوە
        image_url = f"https://pollinations.ai{clean_prompt}?width=1024&height=1024&seed={seed}&enhance=true"
        
        with st.spinner('🎨 چاوەڕێ بکە مامۆستا گیان...'):
            st.image(image_url, caption="ئەمەش وێنەکە بەبێ Error!", use_container_width=True)
            st.markdown(f"**[📥 دابەزاندنی وێنەکە]({image_url})**")
    else:
        st.warning("تکایە سەرەتا شتێک بنووسە.")
