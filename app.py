import streamlit as st
import os

# إعداد الواجهة
st.set_page_config(page_title="Kurdish AI Video", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stMarkdown, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background-color: #FF4B4B; color: white; border-radius: 12px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎥 دروستکەری ڤیدیۆی زیرەک")
st.subheader("وەسفی ڤیدیۆکە بە زمانی کوردی بنووسە")

sorani_input = st.text_area("چی لە خەیاڵتە؟", placeholder="بۆ نموونە: پیاوێکی کورد لە ناو قەڵای هەولێر...")

if st.button("دروستکردنی ڤیدیۆ"):
    if sorani_input.strip():
        with st.spinner('خەریکی دروستکردنی ڤیدیۆکەین... تکایە چاوەڕێ بکە'):
            try:
                from gradio_client import Client
                
                # إرسال النص مباشرة للمحرك مع إضافة وصف سينمائي
                # الذكاء الاصطناعي الحديث بدأ يفهم كلمات مثل (Kurd, Kurdistan, Erbil) حتى لو كتبت بالكردية
                final_prompt = f"{sorani_input}, cinematic style, 4k, realistic, historical"

                client = Client("THUDM/CogVideoX-5B-Space")
                result = client.predict(
                    prompt=final_prompt,
                    seed=42,
                    api_name="/generate"
                )

                if result and os.path.exists(result):
                    st.success("ڤیدیۆکە بە سەرکەوتوویی دروستکرا!")
                    st.video(result)
                    with open(result, "rb") as f:
                        st.download_button("📥 دابەزاندنی ڤیدیۆکە", f, "video.mp4")
                else:
                    st.error("سێرڤەرەکە وەڵامی نەبوو.")
            except Exception as e:
                # هذا السطر سيظهر لنا الخطأ الحقيقي إذا لم يكن من المترجم
                st.error(f"کێشەیەک لە سێرڤەر هەیە: {str(e)}")
    else:
        st.warning("تکایە وەسفێک بنووسە!")
