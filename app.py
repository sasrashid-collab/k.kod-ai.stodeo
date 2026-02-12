import streamlit as st
import random

# ١. دیزاینی شاشە
st.set_page_config(page_title="وێنەسازی کوردی", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background: #28a745; color: white; border-radius: 12px; height: 3.5em; font-weight: bold; border: none; }
    .img-box { width: 100%; border-radius: 15px; border: 2px solid #ddd; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎨 وێنەسازی زیرەکی کوردی")
st.subheader("بە کوردی بنووسە چیت دەوێت:")

user_ku = st.text_area("وەسفی وێنە:", placeholder="بۆ نموونە: قەڵای هەولێر لە داهاتوودا...")

if st.button("✨ وێنەکە دروست بکە"):
    if user_ku.strip():
        # دروستکردنی لوتکەی لینکەکە
        clean_prompt = user_ku.replace(" ", "%20")
        seed = random.randint(0, 999999)
        # بەکارهێنانی لینکی ڕاستەوخۆ کە براوزەر خۆی دەیهێنێت
        image_url = f"https://image.pollinations.ai{clean_prompt}?width=1024&height=1024&seed={seed}&nologo=true"
        
        with st.spinner('🎨 خەریکی کێشانین...'):
            # نیشاندانی وێنەکە ڕاستەوخۆ (ئەمە قەت کێشەی ئینتەرنێتی کۆدەکەی نابێت)
            st.image(image_url, use_container_width=True)
            
            # ڕێنمایی سادە بۆ دابەزاندن
            st.markdown(f"""
                <div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; text-align: right; direction: rtl; border-right: 5px solid #28a745;">
                <b>📥 چۆن وێنەکە پاشکەوت دەکەیت؟</b><br>
                ١. ئەگەر بە <b>مۆبایل</b>یت: پەنجە لەسەر وێنەکە دابگرە و (Download Image) هەڵبژێرە.<br>
                ٢. ئەگەر بە <b>کۆمپیوتەر</b>یت: کلیکی ڕاست لەسەر وێنەکە بکە و (Save Image As) هەڵبژێرە.
                </div>
            """, unsafe_allow_html=True)
            
            # دانانی لینکەکەش بۆ ئەگەرێکی تر
            st.markdown(f"[🔗 کردنەوەی وێنەکە لە پەڕەیەکی نوێ]({image_url})")
    else:
        st.warning("تکایە سەرەتا شتێک بنووسە.")
