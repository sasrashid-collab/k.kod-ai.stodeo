import streamlit as st
import random

# ١. دیزاینی شاشە
st.set_page_config(page_title="وێنەساز", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background: #2ecc71; color: white; border-radius: 12px; height: 3.5em; font-weight: bold; }
    .download-btn {
        display: block; width: 100%; text-align: center; background-color: #3498db;
        color: white; padding: 10px; margin-top: 10px; border-radius: 10px;
        text-decoration: none; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎨 وێنەسازی خێرا بە زمانی کوردی")
st.subheader("بە کوردی بنووسە چیت دەوێت:")

user_ku = st.text_area("چی دروست بکەم؟", placeholder="بۆ نموونە: پیاوێکی کورد بە جلی کوردییەوە...")

if st.button("✨ ئێستا وێنەکە بکێشە"):
    if user_ku.strip():
        clean_prompt = user_ku.replace(" ", "%20")
        seed = random.randint(0, 999999)
        image_url = f"https://pollinations.ai{clean_prompt}?width=1024&height=1024&seed={seed}&enhance=true"
        
        with st.spinner('🎨 چاوەڕێ بکە مامۆستا گیان...'):
            # نیشاندانی وێنەکە
            st.image(image_url, use_container_width=True)
            
            # ٢. دوگمەی دابەزاندنی زیرەک بە HTML (ئەمە قەت Error نادات)
            download_html = f'''
                <a href="{image_url}" download="my_image_{seed}.jpg" target="_blank" class="download-btn">
                    📥 کرتە لێرە بکە بۆ دابەزاندنی وێنەکە
                </a>
            '''
            st.markdown(download_html, unsafe_allow_html=True)
            st.info("تێبینی: ئەگەر وێنەکە نەبووە فایل، لەسەر وێنەکە پەنجە داگرە و Save Image بکە.")
    else:
        st.warning("تکایە سەرەتا شتێک بنووسە.")
