'''
The app allows users to upload an image, adjust the compression quality with a slider, and download the compressed image. 
It also displays the original and compressed images side by side with their respective sizes in KB.
'''
import streamlit as st
from PIL import Image
from io import BytesIO
import os


# Function to compress image
def compress_image(image, quality):
    buffer = BytesIO()
    image.save(buffer, format="JPEG", optimize=True, quality=quality)
    buffer.seek(0)
    return buffer


# Function to get image size in KB
def get_size_kb(buffer):
    return round(len(buffer.getvalue()) / 1024, 2)


# Streamlit UI
st.title("Image Compressor")

st.write("Upload an image and compress it by adjusting the quality slider.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")

    # Original size
    original_buffer = BytesIO()
    image.save(original_buffer, format="JPEG", quality=100)
    original_buffer.seek(0)
    original_size = get_size_kb(original_buffer)

    # Quality slider
    quality = st.slider("Compression Quality", min_value=10, max_value=95, value=75, step=5)

    # Compress image
    compressed_buffer = compress_image(image, quality)
    compressed_size = get_size_kb(compressed_buffer)

    # Preview and size comparison
    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption=f"Original Image ({original_size} KB)", use_container_width=True)
    with col2:
        st.image(compressed_buffer, caption=f"Compressed Image ({compressed_size} KB)", use_container_width=True)

    # Download button
    st.download_button("Download Compressed Image", compressed_buffer, file_name="compressed.jpg", mime="image/jpeg")
