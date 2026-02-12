import streamlit as st
import random

# ١. دیزاینی شاشە
st.set_page_config(page_title="وێنەسازی کوردی", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background: #2ecc71; color: white; border-radius: 12px; height: 3.5em; font-weight: bold; }
    .img-box { width: 100%; border-radius: 15px; border: 3px solid #eee; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎨 وێنەسازی بێ کێشە")
st.subheader("بە کوردی بنووسە چیت دەوێت:")

user_ku = st.text_area("وەسفی وێنە:", placeholder="بۆ نموونە: شارێکی کوردی لە داهاتوودا...")

if st.button("✨ ئێستا وێنەکە دروست بکە"):
    if user_ku.strip():
        # دروستکردنی لوتکەی لینکەکە
        clean_prompt = user_ku.replace(" ", "%20")
        seed = random.randint(0, 999999)
        image_url = f"https://image.pollinations.ai{clean_prompt}?width=1024&height=1024&seed={seed}&nologo=true"
        
        with st.spinner('🎨 خەریکی کێشانین...'):
            # نیشاندانی وێنەکە ڕاستەوخۆ لە ڕێگەی st.image (ئەمە بلۆک نابێت)
            st.image(image_url, use_container_width=True)
            
            # ڕێنمایی پاشکەوتکردن بۆ گەنجەکە بە زمانی کوردی
            st.markdown(f"""
                <div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; text-align: right; direction: rtl; border-right: 5px solid #2ecc71;">
                <b>📥 چۆن وێنەکە پاشکەوت دەکەیت؟</b><br>
                بەهۆی پاراستنی مۆبایلەکەت، کلیک کار ناکات. تکایە <b>پەنجە لەسەر وێنەکە دابگرە</b> و بژاردەی <b>(Download Image)</b> یان <b>(Save Image)</b> هەڵبژێرە.
                </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("تکایە سەرەتا شتێک بنووسە.")
