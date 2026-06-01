'''
This app allows users to upload an image, specify new dimensions, and download the resized image.
'''
import streamlit as st
from PIL import Image
from io import BytesIO

# Function to resize image
def resize_image(image, new_width, new_height):
    return image.resize((new_width, new_height))


# Streamlit UI
st.title("📏 Image Resizer")

st.write("Upload an image and resize it to your preferred dimensions.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    width, height = image.size

    st.subheader("Original Dimensions")
    st.text(f"{width} x {height} px")
    
    # User inputs for new dimensions
    st.subheader("Resize Controls")
    col1, col2 = st.columns(2)
    with col1:
        new_width = st.number_input("New Width (px)", min_value=1, value=width)
    with col2:
        new_height = st.number_input("New Height (px)", min_value=1, value=height)

    # Resize image
    resized_image = resize_image(image, new_width, new_height)

    # Show side-by-side
    st.subheader("Preview")
    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption="Original", use_container_width=True)
    with col2:
        st.image(resized_image, caption="Resized", use_container_width=True)

    # Dowload button
    buffer = BytesIO()
    resized_image.save(buffer, format="PNG")
    buffer.seek(0)
    st.download_button("Download Resized Image", buffer, file_name="resized.png", mime="image/png")

