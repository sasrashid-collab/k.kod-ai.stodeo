import streamlit as st
import random
import requests
import base64

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

user_ku = st.text_area("چی دروست بکەم؟", placeholder="بۆ نموونە: پڵنگێک لەناو بەفردا...")

if st.button("✨ ئێستا وێنەکە بکێشە"):
    if user_ku.strip():
        clean_prompt = user_ku.replace(" ", "%20")
        seed = random.randint(0, 999999)
        image_url = f"https://pollinations.ai{clean_prompt}?width=1024&height=1024&seed={seed}&enhance=true"
        
        with st.spinner('🎨 چاوەڕێ بکە مامۆستا گیان...'):
            try:
                # نیشاندانی وێنەکە
                st.image(image_url, use_container_width=True)
                
                # ٢. چارەسەری کۆتایی: وەرگرتنی وێنەکە و گۆڕینی بۆ فایلی ناوخۆیی
                response = requests.get(image_url)
                if response.status_code == 200:
                    img_bytes = response.content
                    
                    # دوگمەی دابەزاندنی ڕاستەقینە
                    st.download_button(
                        label="📥 دابەزاندنی وێنەکە (بە گەرەنتی)",
                        data=img_bytes,
                        file_name=f"kurd_ai_{seed}.jpg",
                        mime="image/jpeg"
                    )
                else:
                    st.warning("وێنەکە دروست بووە، بەڵام سێرڤەر ڕێگری لە دابەزاندن دەکات. پەنجە بنێ بە وێنەکە بۆ پاشکەوتکردن.")
            except:
                st.error("کێشەیەک لە وەرگرتنی فایلەکە هەبوو.")
    else:
        st.warning("تکایە سەرەتا شتێک بنووسە.")
