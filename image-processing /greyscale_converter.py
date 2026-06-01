'''
Greyscale Image Converter using Streamlit 
'''

import streamlit as st
from PIL import Image
import numpy as np
from io import BytesIO


# Function to convert to grayscale
def convert_to_greyscale(image):
    return image.convert('L') # 'L' mode = greyscale in PIL

# App title
st.title('🖤 Greyscle Image Converter')

st.write('Upload a color image to convert it into grayscale.')


# File uploader
uploaded_file = st.file_uploader('Choose an image...', type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    
    # Process image
    grayscale_image = convert_to_greyscale(image)
    
    # Display original and grayscale side-by-side
    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption="🎨 Original", use_container_width=True)
    with col2:
        st.image(grayscale_image, caption="🖤 Grayscale", use_container_width=True)

    # Download grayscale image
    buffer = BytesIO()
    grayscale_image.save(buffer, format="PNG")
    buffer.seek(0)
    st.download_button("Download Grayscale Image", buffer, file_name="grayscale.png", mime="image/png")
