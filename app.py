import streamlit as st
import requests
import random

# ١. دیزاین و ستایلی ڕەنگاوڕەنگ
st.set_page_config(page_title="وێنەساز و ڤیدیۆساز", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stTitle, .stSubheader { text-align: right; direction: rtl; color: #1E293B; }
    .stButton>button { 
        width: 100%; 
        background: linear-gradient(90deg, #10B981 0%, #3B82F6 100%); 
        color: white; border-radius: 12px; height: 3.5em; font-weight: bold; border: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎨 دروستکەری وێنەی خێرا و جێگیر")
st.subheader("وەسفێک بنووسە بۆ دروستکردن")

# ٢. وەرگرتنی وەسف
user_prompt = st.text_area("وەسف (Prompt):", placeholder="Example: A futuristic Kurdish city, 4k...")

if st.button("✨ ئێستا دروستی بکە"):
    if user_prompt.strip():
        with st.spinner('🎨 خەریکی کێشانی وێنەکەین...'):
            try:
                # بەکارهێنانی Pollinations AI (هەمیشە ئۆنلاین و بێ کێشە)
                seed = random.randint(0, 99999)
                image_url = f"https://image.pollinations.ai{user_prompt}?width=1024&height=1024&seed={seed}&model=flux"
                
                # نیشاندانی وێنەکە
                st.image(image_url, caption="فەرموو مامۆستا گیان، ئەم وێنەیە قەت Error نادات", use_container_width=True)
                
                # دوگمەی دابەزاندن
                response = requests.get(image_url)
                if response.status_code == 200:
                    st.download_button("📥 دابەزاندنی وێنەکە", response.content, "image.jpg", "image/jpeg")
                
            except Exception as e:
                st.error("ببوورە، کێشەیەک لە پەیوەندی ئینتەرنێت هەیە.")
    else:
        st.warning("تکایە سەرەتا وەسفێک بنووسە.")

st.info("ئەم سێرڤەرە زۆر خێرایە و قەت پەیامی 'قەرەباڵغم' نادات.")
