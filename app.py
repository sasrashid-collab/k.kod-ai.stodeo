import streamlit as st
import requests
import base64
import random

st.set_page_config(page_title="وێنەسازی کوردی", layout="centered")

st.markdown("<style>.stTextArea, .stTitle { text-align: right; direction: rtl; }</style>", unsafe_allow_html=True)
st.title("🎨 وێنەسازی (هەوڵی کۆتایی)")

user_ku = st.text_area("وەسفی وێنە:", placeholder="بۆ نموونە: قەڵای هەولێر...")

if st.button("✨ تاقی بکەرەوە"):
    if user_ku.strip():
        with st.spinner('🎨 چاوەڕێ بکە...'):
            try:
                # بەکارهێنانی لینکێکی جیاوازتر کە کەمتر بلۆک دەکرێت
                seed = random.randint(0, 999999)
                url = f"https://pollinations.ai{user_ku.replace(' ', '%20')}?width=1024&height=1024&seed={seed}&model=flux&nologo=true"
                
                # وەرگرتنی وێنەکە بە شێوازێکی فەرمیتر
                headers = {'User-Agent': 'Mozilla/5.0'}
                response = requests.get(url, headers=headers, timeout=20)
                
                if response.status_code == 200:
                    encoded_img = base64.b64encode(response.content).decode()
                    st.markdown(f'<img src="data:image/jpeg;base64,{encoded_img}" style="width:100%; border-radius:15px;">', unsafe_allow_html=True)
                    st.success("سەرکەوتوو بوو مامۆستا!")
                else:
                    st.error(f"سێرڤەر وەڵامی نییە (کۆد: {response.status_code})")
            except Exception as e:
                st.error("هێشتا کێشەی پەیوەندی هەیە.")
    else:
        st.warning("شتێک بنووسە.")
