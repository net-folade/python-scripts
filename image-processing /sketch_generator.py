'''
Adjust the blur and intensity to get different styles of sketches.
'''
import streamlit as st
from PIL import Image
import numpy as np
import cv2
from io import BytesIO


# Pencil sketch effect
def pencil_sketch(image, blur_ksize=21, intensity=1.0):
    img_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_blur = cv2.GaussianBlur(img_invert, (blur_ksize, blur_ksize), sigmaX=0, sigmaY=0)
    sketch = cv2.divide(img_gray, 255 - img_blur, scale=256 * intensity)
    return sketch


# Streamlit UI
st.title("✏️ Pencil Sketch Converter")

st.write("Upload a photo to turn it into a pencil sketch.")

# Upload file
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

st.subheader("Sketch Settings")
blur_value = st.slider("Blur Sharpness", 1, 51, 21, step=2)  # Must be odd
intensity = st.slider("Sketch Intensity", 0.1, 2.0, 1.0, step=0.1)

# Process and display images
if uploaded_file:
    pil_image = Image.open(uploaded_file).convert("RGB")
    image = np.array(pil_image)

    # Pass user-defined blur and intensity
    sketch_image = pencil_sketch(image, blur_ksize=blur_value, intensity=intensity)

    # Show original and sketch side-by-side
    col1, col2 = st.columns(2)
    with col1:
        st.image(pil_image, caption="Original", use_container_width=True)
    with col2:
        st.image(sketch_image, caption="Sketch", use_container_width=True)

    # Download
    sketch_pil = Image.fromarray(sketch_image)
    buffer = BytesIO()
    sketch_pil.save(buffer, format="PNG")
    buffer.seek(0)
    st.download_button("Download Sketch", buffer, file_name="sketch.png", mime="image/png")
