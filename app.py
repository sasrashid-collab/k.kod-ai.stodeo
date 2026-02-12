import streamlit as st
from gradio_client import Client

# ١. دیزاین و ستایلی ڕەنگاوڕەنگ
st.set_page_config(page_title="دیزاینەری زیرەک", layout="centered")

st.markdown("""
    <style>
    .stTextArea, .stTitle, .stSubheader { text-align: right; direction: rtl; color: #2D3748; }
    .stButton>button { 
        width: 100%; 
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); 
        color: white; border-radius: 12px; height: 3.5em; font-weight: bold; border: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎨 دروستکەری وێنە و ڤیدیۆ")
st.subheader("وەسفێک بنووسە بۆ دروستکردن")

# ٢. وەرگرتنی وەسف
user_prompt = st.text_area("وەسف (Prompt):", placeholder="Example: A futuristic city, 4k...")

# ٣. هەڵبژاردنی جۆر
option = st.radio("دەتەوێت چی بۆ دروست بکەم؟", ("وێنەی کوالێتی بەرز (خێرا)", "ڤیدیۆی جوڵاو (کەمێک خاو)"))

if st.button("✨ دەستپێکردن"):
    if user_prompt.strip():
        with st.spinner('🎨 خەریکی ئامادەکردنین...'):
            try:
                if option == "وێنەی کوالێتی بەرز (خێرا)":
                    # مۆدێلێکی زۆر جێگیر و هەمیشە ئۆنلاین بۆ وێنە
                    client = Client("stabilityai/stable-diffusion-3.5-large-turbo")
                    result = client.predict(
                        prompt=user_prompt,
                        negative_prompt="",
                        seed=42,
                        width=1024,
                        height=1024,
                        guidance_scale=0.0,
                        num_inference_steps=4,
                        api_name="/infer"
                    )
                    if result:
                        st.image(result, caption="فەرموو مامۆستا گیان", use_container_width=True)
                
                else:
                    # مۆدێلێکی جێگیر بۆ ڤیدیۆ
                    client = Client("aliabd/stable-video-diffusion")
                    result = client.predict(user_prompt, 42, api_name="/generate_video")
                    if result:
                        st.video(result)
                        st.success("فەرموو ڤیدیۆکەت ئامادەیە")
                        
            except Exception as e:
                st.error("سێرڤەرەکە لەم ساتەدا قەرەباڵغە، تکایە دووبارە کلیک بکەرەوە.")
    else:
        st.warning("تکایە سەرەتا وەسفێک بنووسە.")
