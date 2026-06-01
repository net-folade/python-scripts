'''
Users can upload an image, adjust the brush size and intensity using sliders, and download the processed image. 
The original and processed images are displayed side by side for comparison.
'''

import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO


# Function to apply oil painting effect
def oil_painting_effect(image, size, dyn_ratio):
    image = np.array(image)  # Convert to NumPy array
    oil_painting = cv2.xphoto.oilPainting(image, size, dyn_ratio)
    return oil_painting

# Streamlit UI
st.title("🎨 Oil Painting Effect Converter")

st.write("Upload an image and adjust the effect using the sliders below.")

# Sliders for oil painting parameters
size = st.slider("Brush Size (Neighborhood)", min_value=1, max_value=20, value=7, step=1)
dyn_ratio = st.slider("Dynamic Ratio (Intensity)", min_value=1, max_value=100, value=1, step=1)

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    processed_image = oil_painting_effect(image, size, dyn_ratio)

    # Display side-by-side images
    col1, col2 = st.columns(2)

    with col1:
        st.image(image, caption="🖼️ Original Image", use_container_width=True)

    with col2:
        st.image(processed_image, caption="🎭 Oil Painting Effect", use_container_width=True)

    # Download button for the processed image
    img = Image.fromarray(processed_image)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    st.download_button("Download Processed Image", buffer, file_name="oil_painting.png", mime="image/png")
