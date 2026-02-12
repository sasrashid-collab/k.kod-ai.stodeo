import streamlit as st

st.set_page_config(page_title="وێنەساز", layout="centered")

st.markdown("<style>.stTextArea, .stTitle { text-align: right; direction: rtl; }</style>", unsafe_allow_html=True)
st.title("🎨 وێنەسازی کوردی (هەوڵی کۆتایی)")

user_ku = st.text_area("چی دروست بکەم؟", placeholder="بۆ نموونە: قەڵای هەولێر...")

if st.button("✨ وێنەکە نیشان بدە"):
    if user_ku.strip():
        # بەکارهێنانی سێرڤەری گەڕانی وێنەی گووگڵ وەک فێڵێک
        # ئەمە وێنەی ئامادەکراو دەهێنێت نەک دروستکراو، بۆ ئەوەی دڵنیا بین ئینتەرنێتەکەت وێنە دەخوێنێتەوە
        clean_prompt = user_ku.replace(" ", "+")
        image_url = f"https://source.unsplash.com?{clean_prompt}"
        
        st.markdown(f'### فەرموو مامۆستا گیان، ئەگەر ئەمە دەرنەکەوت واتا ئینتەرنێتەکەت وێنەی دەرەکی بلۆک کردووە:')
        st.image(image_url, use_container_width=True)
    else:
        st.warning("تکایە شتێک بنووسە.")
