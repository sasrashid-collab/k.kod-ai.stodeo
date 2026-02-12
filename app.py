import streamlit as st
import random

# ١. ڕێکخستنی لاپەڕە
st.set_page_config(page_title="وێنەسازی کوردی", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background: #28a745; color: white; border-radius: 12px; height: 3.5em; font-weight: bold; }
    .img-frame { width: 100%; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.2); }
    </style>
    """, unsafe_allow_html=True)

st.title("🎨 وێنەسازی کوردی (بێ کێشە)")
st.subheader("وەسفێک بنووسە بە کوردی یان ئینگلیزی:")

user_input = st.text_area("چی دروست بکەم؟", placeholder="بۆ نموونە: ئەسپێکی سپی لەسەر مانگ...")

if st.button("✨ وێنەکە دروست بکە"):
    if user_input.strip():
        # دروستکردنی لوتکەی لینکەکە
        clean_prompt = user_input.replace(" ", "%20")
        seed = random.randint(0, 999999)
        # بەکارهێنانی لینکی ڕاستەوخۆ کە بلۆک نابێت
        image_url = f"https://image.pollinations.ai{clean_prompt}?width=800&height=800&seed={seed}&nologo=true"
        
        with st.spinner('🎨 چاوەڕێ بکە...'):
            # بەکارهێنانی HTML بۆ نیشاندانی وێنەکە تاوەکو سێرڤەر ڕێگری لێ نەکات
            st.markdown(f'<img src="{image_url}" class="img-frame">', unsafe_allow_html=True)
            
            st.markdown(f"""
                <div style="text-align: right; direction: rtl; margin-top: 15px; padding: 10px; background: #f0f2f6; border-radius: 10px;">
                <b>📥 چۆن وێنەکە پاشکەوت دەکەیت؟</b><br>
                پەنجە لەسەر وێنەکە دابگرە و بژاردەی <b>(Download Image)</b> یان <b>(Save Image)</b> هەڵبژێرە.
                <br><br>
                <a href="{image_url}" target="_blank" style="color: #007bff; text-decoration: none;">🔗 کلیک لێرە بکە بۆ بینینی وێنەکە لە پەڕەیەکی تر</a>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("تکایە سەرەتا وەسفێک بنووسە.")
