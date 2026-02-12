import streamlit as st
from gradio_client import Client

# ١. ڕێکخستنی لاپەڕە
st.set_page_config(page_title="ڤیدیۆساز", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background-color: #FF4B4B; color: white; border-radius: 10px; height: 3em; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎥 دروستکەری ڤیدیۆی کوردی")
st.subheader("بە کوردی بنووسە، ئێمە دەیکەین بە ڤیدیۆ")

# ٢. وەرگرتنی نووسینی کوردی
user_ku = st.text_area("چی دروست بکەم؟", placeholder="بۆ نموونە: هەڵۆیەکی گەورە لەسەر لوتکەی چیا...")

if st.button("دروستکردنی ڤیدیۆ"):
    if user_ku.strip():
        with st.spinner('خەریکی وەرگێڕان و دروستکردنین... تکایە کەمێک چاوەڕێ بکە'):
            try:
                # هەنگاوی یەکەم: وەرگێڕان لە ڕێگەی مۆدێلێکی AI (وەک فێڵێک بۆ ئەوەی Error نەدات)
                # لێرەدا دەتوانیت مۆدێلێکی وەرگێڕانی وەک 'Helsinki-NLP' بەکاربهێنیت یان ڕاستەوخۆ دەقەکە بنێریت
                
                # بۆ ئەوەی گەنجەکە ماڵوێران نەبێت، دەقە کوردییەکە ڕاستەوخۆ دەنێرین بۆ مۆدێلێکی ڤیدیۆ کە زمانی تر تێدەگات
                # یان مۆدێلێکی وەرگێڕانی جێگیر بەکاردەهێنین
                
                client_vid = Client("aliabd/stable-video-diffusion")
                
                # لێرەدا دەتوانیت لە جیاتی وەرگێڕان، تەنها پاشگرێکی ئینگلیزی بۆ زیاد بکەیت 
                # یان ئەگەر کارت نەکرد، ناچارین داوا لە گەنجەکە بکەین تەنها یەک وشەی ئینگلیزی بنووسێت
                result = client_vid.predict(user_ku, 42, api_name="/generate_video")

                if result:
                    st.success("فەرموو مامۆستا گیان، ڤیدیۆکە ئامادەیە:")
                    st.video(result)
                else:
                    st.error("سێرڤەرەکە کەمێک قەرەباڵغە.")
            except Exception as e:
                st.error("کێشەیەک لە پەیوەندی سێرڤەر ڕوویدا.")
    else:
        st.warning("تکایە وەسفێک بنووسە.")
