            try:
                if option == "وێنەی کوالێتی بەرز (خێرا)":
                    # مۆدێلێکی جێگیرتر بۆ وێنە
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
                        st.image(result[0], caption="فەرموو مامۆستا گیان", use_container_width=True)
                
                else:
                    # مۆدێلێکی جیاوازتر بۆ ڤیدیۆ
                    client = Client("fffiloni/stable-video-diffusion-img2vid")
                    result = client.predict(user_prompt, 42, api_name="/generate_video")
                    if result:
                        st.video(result)
