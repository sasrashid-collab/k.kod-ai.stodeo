import streamlit as st
import requests
import random

# ١. دیزاینی لاپەڕە
st.set_page_config(page_title="وێنەسازی کوردی", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background: #28a745; color: white; border-radius: 12px; height: 3.5em; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎨 وێنەسازی کوردی (وەشانی جێگیر)")
st.subheader("بە کوردی بنووسە چیت دەوێت:")

user_ku = st.text_area("وەسفی وێنەکە:", placeholder="بۆ نموونە: ئەسپێکی سپی لەناو بەفردا...")

if st.button("✨ وێنەکە دروست بکە"):
    if user_ku.strip():
        # دروستکردنی ناونیشانی وێنە
        clean_prompt = user_ku.replace(" ", "%20")
        seed = random.randint(0, 999999)
        image_url = f"https://image.pollinations.ai{clean_prompt}?width=800&height=800&seed={seed}&nologo=true"
        
        with st.spinner('🎨 خەریکی کێشانی وێنەکەین...'):
            try:
                # هەنگاوی گرنگ: دابەزاندنی وێنەکە بۆ ناو کۆدەکە
                response = requests.get(image_url)
                if response.status_code == 200:
                    # نیشاندانی وێنەکە وەک داتا (نەک وەک لینک)
                    st.image(response.content, use_container_width=True)
                    
                    # دروستکردنی دوگمەی دابەزاندنی ڕاستەقینە
                    st.download_button(
                        label="📥 وێنەکە دابەزێنە ناو مۆبایلەکەت",
                        data=response.content,
                        file_name=f"kurd_ai_{seed}.jpg",
                        mime="image/jpeg"
                    )
                else:
                    st.error("سێرڤەرەکە لەم ساتەدا وەڵامی نییە.")
            except:
                st.error("کێشەیەک لە پەیوەندی ئینتەرنێت هەیە.")
    else:
        st.warning("تکایە سەرەتا شتێک بنووسە.")
