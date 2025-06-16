import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
import streamlit as st

hide_streamlit_cloud_elements = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    a[title="View source"] {display: none !important;}
    button[kind="icon"] {display: none !important;}
    </style>
"""
st.markdown(hide_streamlit_cloud_elements, unsafe_allow_html=True)

st.header("Welcome to Image Resizer")
st.title("Photo Resizer App Using OpenCV")

img = st.file_uploader("Upload an image", type=["jpeg", "png"])

if img:
    img = Image.open(img)
    array_image = np.array(img)
    st.image(array_image, caption="Original Image", width=100)

    width = st.number_input("Enter width", min_value=1, value=array_image.shape[1])
    height = st.number_input("Enter height", min_value=1, value=array_image.shape[0])

    flip_value = st.selectbox("Direction", ["None", "Vertical", "Horizontal"])
    if flip_value == "Vertical":
        array_image = cv2.flip(array_image, 0)
    elif flip_value == "Horizontal":
        array_image = cv2.flip(array_image, 1)

    st.image(array_image, caption="Flipped Image", width=100)

    if st.button("Resize"):
        resized_image = cv2.resize(array_image, (int(width), int(height)))
        st.image(resized_image, caption="Resized Image", width=100)

        buff = BytesIO()
        image_pil = Image.fromarray(resized_image)
        image_pil.save(buff, format="JPEG")

        st.download_button(
            "Download Here",
            data=buff.getvalue(),
            mime="image/jpeg",
            file_name="resized_image.jpeg"
        )
