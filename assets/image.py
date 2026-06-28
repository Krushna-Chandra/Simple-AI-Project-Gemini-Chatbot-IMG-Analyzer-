import streamlit as st
import dotenv
import os
from dotenv import load_dotenv
from PIL import Image
from google import genai

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="AI Image App", page_icon="🖼️", layout="centered")

# ---------- HEADER ----------
st.title("🖼️ AI Image Analyzer")
st.caption("Upload an image and ask AI to describe or analyze it")

st.divider()

# -----------all step by step--------------
# -------step-1-------

load_dotenv()                       # .env file is available or not
Api_key = os.getenv('API_KEY')


#-----------step-2------------------
st.subheader("📤 Upload Image")

# package: pillow
image = st.file_uploader(
    "Upload your image",
    type=['png','jpg','jpeg']
)

if image is not None:
    img = Image.open(image)     # === PIL.Image.open
    st.image(img, caption="Image Preview", use_container_width=True)

# st.divider()

st.subheader("💬 Ask About the Image")

prompt = st.text_input(
    "Enter your prompt",
    placeholder="Example: Describe this image"
)       # st.text input

st.write("")

# -----------step-3----------------
if st.button('🚀 Generate Result', use_container_width=True):

    client = genai.Client(api_key=Api_key)

    # prompt='describe about the image in hindi'     # no need this now
    Input = [img, prompt]              # for not confusing the model that img is available or not

    with st.spinner("Analyzing image..."):

        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=Input
        )

    st.divider()
    st.subheader("📊 AI Response")

    st.success(response.text)