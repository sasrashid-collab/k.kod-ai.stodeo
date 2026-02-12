import streamlit as st
import requests
import base64
import random

st.set_page_config(page_title="وێنەسازی بێ کێشە", layout="centered")

st.markdown("<style>.stTextArea, .stTitle { text-align: right; direction: rtl; }</style>", unsafe_allow_html=True)
st.title("🎨 وێنەسازی کوردی (چارەسەری بنەڕەتی)")

user_ku = st.text_area("وەسفی وێنە بە کوردی:", placeholder="بۆ نموونە: قەڵای هەولێر لە داهاتوودا...")

if st.button("✨ وێنەکە دروست بکە"):
    if user_ku.strip():
        with st.spinner('🎨 خەریکی کێشانین...'):
            try:
                # بەکارهێنانی سێرڤەرێکی جیاواز و گۆڕینی وێنە بۆ کۆد
                seed = random.randint(0, 99999)
                # ئەمجارە بە Requests وێنەکە دەهێنین نەک بە لینک
                img_url = f"https://image.pollinations.ai{user_ku}?seed={seed}&nologo=true"
                
                response = requests.get(img_url)
                if response.status_code == 200:
                    # گۆڕینی وێنەکە بۆ دەق (Base64) بۆ ئەوەی بلۆک نەبێت
                    encoded_img = base64.b64encode(response.content).decode()
                    
                    # نیشاندانی وێنەکە بە فێڵی کۆد
                    st.markdown(f'<img src="data:image/jpeg;base64,{encoded_img}" style="width:100%; border-radius:15px;">', unsafe_allow_html=True)
                    
                    st.success("فەرموو مامۆستا گیان، ئەمجارە مەحاڵە بلۆک بێت!")
                else:
                    st.error("سێرڤەرەکە وەڵامی نەبوو.")
            except:
                st.error("هێشتا ئینتەرنێتەکەت ڕێگری دەکات. فلتەرشکێن (VPN) تاقی بکەرەوە.")
    else:
        st.warning("تکایە شتێک بنووسە.")
