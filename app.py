import streamlit as st
import random
import requests
import io

# ١. ڕێکخستنی شاشە
st.set_page_config(page_title="وێنەسازی کوردی", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background: #28a745; color: white; border-radius: 12px; height: 3.5em; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎨 وێنەسازی زیرەکی کوردی")
st.subheader("بە کوردی بنووسە چیت دەوێت:")

user_ku = st.text_area("وەسفی وێنە:", placeholder="بۆ نموونە: دیمەنێکی جوانی کوردستان لە بەهاردا...")

if st.button("✨ وێنەکە دروست بکە"):
    if user_ku.strip():
        # دروستکردنی لینکەکە
        clean_prompt = user_ku.replace(" ", "%20")
        seed = random.randint(0, 999999)
        image_url = f"https://image.pollinations.ai{clean_prompt}?width=1024&height=1024&seed={seed}&nologo=true"
        
        with st.spinner('🎨 خەریکی کێشانین... تکایە چاوەڕێ بکە'):
            try:
                # وەرگرتنی داتای وێنەکە لە سێرڤەرەوە
                response = requests.get(image_url, timeout=30)
                if response.status_code == 200:
                    image_bytes = response.content
                    
                    # نیشاندانی وێنەکە
                    st.image(image_bytes, use_container_width=True)
                    
                    # دوگمەی دابەزاندنی فەرمی ستریملێت (ئەمە بلۆک نابێت)
                    st.download_button(
                        label="📥 دابەزاندنی وێنەکە بۆ ناو ئامێرەکەت",
                        data=image_bytes,
                        file_name=f"kurd_ai_{seed}.jpg",
                        mime="image/jpeg"
                    )
                else:
                    st.error("سێرڤەرەکە کەمێک قەرەباڵغە، کەمێکی تر تاقی بکەرەوە.")
            except Exception as e:
                st.error("کێشەیەک لە پەیوەندی دروست بوو. دڵنیابە لە ئینتەرنێتەکەت.")
    else:
        st.warning("تکایە سەرەتا شتێک بنووسە.")
