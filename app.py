import streamlit as st
from dotenv import load_dotenv
import os
from PIL import Image
import google.generativeai as genai
from google import genai as new_genai

# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="Gemini AI",
    page_icon="🤖",
    layout="centered"
)

# LOAD API
# ---------------------------
load_dotenv()

API_KEY = os.getenv("API_KEY")

genai.configure(api_key=API_KEY)

chat_model = genai.GenerativeModel("gemini-2.5-flash")
client = new_genai.Client(api_key=API_KEY)

# SESSION STATE
# ---------------------------
if "mode" not in st.session_state:
    st.session_state.mode = "chat"

# =====================================================
# CHAT MODE
# =====================================================

if st.session_state.mode == "chat":

    st.title("🤖 Gemini AI")
    if st.button("➕ Add Image"):
        st.session_state.mode = "image"
        st.rerun()
    prompt = st.chat_input("Type your message...")
    if prompt:

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.spinner("Thinking..."):
            response = chat_model.generate_content(prompt)

        with st.chat_message("assistant"):
            st.markdown(response.text)

# IMAGE MODE
# =====================================================

else:

    st.title("🖼️ AI Image Analyzer")
    st.caption("Upload an image and ask AI to describe or analyze it")
    # st.divider()
        # Upload Image
    st.subheader("📤 Upload Image")

    image = st.file_uploader(
        "Upload your image",
        type=["png", "jpg", "jpeg"]
    )

    img = None
    if image is not None:
        img = Image.open(image)
        st.image(
            img,
            caption="Image Preview",
            use_container_width=True
        )

    st.divider()

    # Prompt
    st.subheader("💬 Ask About the Image")

    prompt = st.text_input(
        "Enter your prompt",
        placeholder="Example: Describe this image"
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("⬅ Back to Chat", use_container_width=True):
            st.session_state.mode = "chat"
            st.rerun()

    with col2:

        analyze = st.button(
            "🚀 Generate Result",
            use_container_width=True
        )

    if analyze:

        if img is None:
            st.warning("Please upload an image.")

        elif prompt.strip() == "":
            st.warning("Please enter a prompt.")

        else:

            with st.spinner("Analyzing image..."):

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=[img, prompt]
                )

            st.divider()

            st.subheader("📊 AI Response")

            st.markdown(response.text)