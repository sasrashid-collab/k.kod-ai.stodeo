import streamlit as st
import random

# ١. ڕێکخستنی شاشە
st.set_page_config(page_title="وێنەسازی کوردی", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background: #2ecc71; color: white; border-radius: 12px; height: 3.5em; font-weight: bold; border: none; }
    .image-container { text-align: center; margin-top: 20px; }
    .image-container img { width: 100%; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

st.title("🎨 وێنەسازی کوردی (وەشانی بێ کێشە)")
st.subheader("بە کوردی بنووسە چیت دەوێت:")

user_ku = st.text_area("وەسفی وێنە:", placeholder="بۆ نموونە: شارێکی کوردی لە ساڵی ٢٠٥٠...")

if st.button("✨ ئێستا وێنەکە دروست بکە"):
    if user_ku.strip():
        # دروستکردنی لوتکەی لینکەکە
        clean_prompt = user_ku.replace(" ", "%20")
        seed = random.randint(0, 999999)
        image_url = f"https://image.pollinations.ai{clean_prompt}?width=1024&height=1024&seed={seed}&nologo=true"
        
        with st.spinner('🎨 خەریکی کێشانین...'):
            # بەکارهێنانی HTML بۆ نیشاندانی ڕاستەوخۆ (ئەمە بلۆک نابێت)
            st.markdown(f'''
                <div class="image-container">
                    <img src="{image_url}">
                </div>
                <div style="text-align: right; direction: rtl; margin-top: 15px; padding: 15px; background: #f0f2f6; border-radius: 10px;">
                    <b>📥 چۆن وێنەکە پاشکەوت دەکەیت؟</b><br>
                    ١. لەسەر وێنەکە <b>کلیکی ڕاست</b> بکە.<br>
                    ٢. بژاردەی <b>(Save Image As)</b> یان <b>(پاشکەوتکردنی وێنە)</b> هەڵبژێرە.
                </div>
            ''', unsafe_allow_html=True)
    else:
        st.warning("تکایە سەرەتا شتێک بنووسە.")
