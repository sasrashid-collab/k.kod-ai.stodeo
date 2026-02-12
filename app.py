import streamlit as st
import random

# ١. ڕێکخستنی شاشە
st.set_page_config(page_title="وێنەساز", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { 
        width: 100%; 
        background: linear-gradient(90deg, #FF4B4B, #FF9900); 
        color: white; border-radius: 12px; height: 3.5em; font-weight: bold; border: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎨 دروستکەری وێنەی خێرا")
st.subheader("وەسفێک بە ئینگلیزی بنووسە:")

# ٢. وەرگرتنی وەسف
user_prompt = st.text_area("چی بکێشم؟", placeholder="Example: A lion in Erbil city...")

if st.button("✨ ئێستا دروستی بکە"):
    if user_prompt.strip():
        # دروستکردنی لوتکەی لینکەکە بە شێوەیەکی زیرەک
        # ئەم ڕێگەیە پێویستی بە requests نییە و ڕاستەوخۆ وێنەکە نیشان دەدات
        clean_prompt = user_prompt.replace(" ", "%20")
        seed = random.randint(0, 999999)
        image_url = f"https://pollinations.ai{clean_prompt}?width=1024&height=1024&seed={seed}"
        
        with st.spinner('خەریکی کێشانین...'):
            # نیشاندانی وێنەکە ڕاستەوخۆ لە ڕێگەی مارکداون یان ستێملێت
            st.image(image_url, caption="فەرموو مامۆستا گیان، ئەمجارە ناتوانێت بڵێت Error!", use_container_width=True)
            
            st.markdown(f"[🔗 لینکی وێنەکە بۆ دابەزاندن]({image_url})")
    else:
        st.warning("تکایە وەسفەکە بنووسە.")

st.info("ئەم ڕێگەیە بەکارهێنانی لینکی ڕاستەوخۆیە و قەت پەککەوتنی سێرڤەری Gradio نایگرێتەوە.")
