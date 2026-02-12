import streamlit as st
import random

# ١. دیزاینی شاشە
st.set_page_config(page_title="وێنەساز", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stTitle, .stSubheader { text-align: right; direction: rtl; }
    .stButton>button { width: 100%; background: #2ecc71; color: white; border-radius: 12px; height: 3.5em; font-weight: bold; }
    .guide-box { 
        background-color: #f0f2f6; padding: 15px; border-radius: 10px; 
        border-right: 5px solid #3498db; text-align: right; direction: rtl;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎨 وێنەسازی خێرا بە زمانی کوردی")
st.subheader("بە کوردی بنووسە چیت دەوێت:")

user_ku = st.text_area("چی دروست بکەم؟", placeholder="بۆ نموونە: شارێکی کوردی لە داهاتوودا...")

if st.button("✨ ئێستا وێنەکە بکێشە"):
    if user_ku.strip():
        # چاککردنی لینکەکە (زیادکردنی /p/ کە لە کۆدەکەی پێشترتدا نەمابوو)
        clean_prompt = user_ku.replace(" ", "%20")
        seed = random.randint(0, 999999)
        image_url = f"https://pollinations.ai{clean_prompt}?width=1024&height=1024&seed={seed}&enhance=true"
        
        with st.spinner('🎨 چاوەڕێ بکە مامۆستا گیان...'):
            # نیشاندانی وێنەکە
            st.image(image_url, use_container_width=True)
            
            # ٢. ڕێنمایی بۆ دابەزاندن
            st.markdown(f"""
            <div class="guide-box">
                <b>📥 چۆن وێنەکە پاشکەوت دەکەیت؟</b><br>
                ١. ئەگەر بە <b>مۆبایل</b>یت: پەنجە لەسەر وێنەکە دابگرە و (Download Image) هەڵبژێرە.<br>
                ٢. ئەگەر بە <b>کۆمپیوتەر</b>یت: کلیکی ڕاست لەسەر وێنەکە بکە و (Save Image As) هەڵبژێرە.
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"[🔗 لینکی ڕاستەوخۆی وێنەکە]({image_url})")
    else:
        st.warning("تکایە سەرەتا شتێک بنووسە.")
