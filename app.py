import streamlit as st
import requests
import os

# 1. إعداد الواجهة الكوردية
st.set_page_config(page_title="دروستکەری ڤیدیۆ", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stMarkdown, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background-color: #FF4B4B; color: white; border-radius: 12px; height: 3em; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎥 دروستکەری ڤیدیۆی زیرەک")
st.subheader("وەسفی ڤیدیۆکە بە زمانی کوردی بنووسە")

# 2. وظيفة المترجم التلقائي (يغذي البرومبت مباشرة)
def auto_translate_prompt(text):
    try:
        # استخدام رابط مباشر يتجاهل أخطاء اللغة ويحول أي نص إلى إنجليزية فوراً
        url = f"https://translate.googleapis.com{text}"
        r = requests.get(url).json()
        return r[0][0][0] # استخراج النص المترجم الصافي
    except:
        return text # في حال الفشل يرسل النص كما هو

# 3. خانة النص الكوردي
sorani_input = st.text_area("چی لە خەیاڵتە؟", placeholder="بۆ نموونە: قەڵای هەولێر...")

if st.button("دروستکردنی ڤیدیۆ"):
    if sorani_input.strip():
        with st.spinner('خەریکی وەرگێڕان و دروستکردنی ڤیدیۆکەین...'):
            try:
                from gradio_client import Client
                
                # المترجم يضع النتيجة في البرومبت (Prompt) تلقائياً هنا
                translated_prompt = auto_translate_prompt(sorani_input)
                
                # إضافة اللمسة السينمائية للأمر النهائي
                final_prompt = f"{translated_prompt}, cinematic style, 4k, realistic"
                
                # إرسال الأمر للمحرك
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
                st.error(f"هەڵەیەک ڕوویدا: {str(e)}")
    else:
        st.warning("تکایە وەسفێک بنووسە!")
