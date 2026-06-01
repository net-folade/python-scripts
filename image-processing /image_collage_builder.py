'''
Collage builder - Upload multiple images and arrange them in a grid layout. 
'''
import streamlit as st
from PIL import Image
from io import BytesIO
import math


# Function to create collage
def create_collage(images, cols):
    rows = math.ceil(len(images) / cols)
    thumb_width, thumb_height = images[0].size

    collage_width = cols * thumb_width
    collage_height = rows * thumb_height

    collage = Image.new('RGB', (collage_width, collage_height), color=(255, 255, 255))

    for index, img in enumerate(images):
        row = index // cols
        col = index % cols
        x = col * thumb_width
        y = row * thumb_height
        collage.paste(img, (x, y))

    return collage


# Streamlit UI
st.title("Image Collage Builder")

st.write("Upload multiple images and arrange them in a grid layout.")

uploaded_files = st.file_uploader("Upload images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files:
    # Load and resize all images to same size
    st.subheader("Thumbnail Size (for all images)")
    width = st.slider("Width", 50, 500, 200)
    height = st.slider("Height", 50, 500, 200)

    images = [Image.open(file).resize((width, height)) for file in uploaded_files]

    st.subheader("Choose Collage Layout")
    cols = st.slider("Number of Columns", 1, 5, 2)

    collage_image = create_collage(images, cols)

    st.image(collage_image, caption="🧩 Collage", use_container_width=True)

    # Download
    buffer = BytesIO()
    collage_image.save(buffer, format="PNG")
    buffer.seek(0)
    st.download_button("Download Collage", buffer, file_name="collage.png", mime="image/png")
