import streamlit as st
from gradio_client import Client

# ١. ڕێکخستنی شاشە
st.set_page_config(page_title="ڤیدیۆساز بە کوردی", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background-color: #FF4B4B; color: white; border-radius: 10px; height: 3em; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎥 دروستکەری ڤیدیۆ بە زمانی کوردی")
st.subheader("بە کوردی بنووسە، ئێمە دەیکەین بە ڤیدیۆ")

# ٢. وەرگرتنی نووسینی کوردی
user_ku = st.text_area("چی دروست بکەم؟", placeholder="بۆ نموونە: ئەسپێکی سپی لەناو دارستانێکی چڕدا...")

if st.button("دروستکردنی ڤیدیۆ"):
    if user_ku.strip():
        with st.spinner('خەریکە بە زمانی کوردی ڤیدیۆکەت بۆ دروست دەکەین...'):
            try:
                # بەکارهێنانی مۆدێلێک کە زمانی تریش تێدەگات (وەک CogVideo) 
                # بۆ ئەوەی گەنجەکە ماڵوێران نەبێت
                client = Client("THUDM/CogVideoX-5B-Space")
                
                # لێرەدا دەقە کوردییەکە ڕاستەوخۆ دەنێرین، چونکە ئەم مۆدێلە توانای تێگەیشتنی زیاترە
                result = client.predict(
                    user_ku, # کوردییەکە وەک خۆی
                    42,      # Seed
                    6,       # Guidance
                    50,      # Steps
                    api_name="/generate"
                )

                if result:
                    st.success("فەرموو مامۆستا گیان، ڤیدیۆکە ئامادەیە:")
                    st.video(result)
                else:
                    st.error("سێرڤەرەکە قەرەباڵغە، تکایە دووبارە دایگرەوە.")
            except Exception as e:
                st.error("کێشەیەک لە سێرڤەر هەیە. تکایە جارێکی تر تاقی بکەرەوە.")
    else:
        st.warning("تکایە وەسفەکە بنووسە.")
