import streamlit as st
import base64

def get_image_base64(image_path):
    """
    Converts a local image to a Base64 string.
    """
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def circular_image(image_url: str):
    """
    Displays an image within a circle.
    """

    base64_image = get_image_base64(image_url)
    image_data_url = f"data:image/png;base64,{base64_image}"

    st.markdown(
        f"""
        <style>
        .circular-img {{
            width: 350px;
            height: 350px;
            object-fit: contain;
            border-radius: 50%;
            border: 2px solid #ddd;
            display: block;
        }}
        </style>
        <img src="{image_data_url}" class="circular-img" />
        """,
        unsafe_allow_html=True
    )

