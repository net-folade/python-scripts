'''
This app allows users to upload an image, 
select a desired aspect ratio, and crop the image accordingly. 
The cropped image can then be downloaded directly from the app.
'''
import streamlit as st 
from PIL import Image
import numpy as np
import io

# Streamlit UI
st.title('Image Cropper with Aspect Ratio')
st.write('Upload an image and crop it with a fixed aspect ratio!')

# Upload image
uploaded_img = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_img is not None:
    # Open and display the original image
    image = Image.open(uploaded_img).convert('RGB')
    st.image(image, caption='Original Image', use_column_width=True)
    
    # Get image dimensions
    width, height = image.size

    # Aspect ratio options
    aspect_ratios = {"1:1 (Square)": 1/1, "4:3": 4/3, "3:4": 3/4, "16:9": 16/9, "9:16": 9/16}
    selected_ratio_name = st.selectbox("Choose aspect ratio", list(aspect_ratios.keys()))
    aspect_ratio = aspect_ratios[selected_ratio_name]

    # Calculate maximum crop dimensions based on aspect ratio
    if aspect_ratio >= 1:  # Wider than tall (e.g., 4:3, 16:9)
        max_crop_width = width
        max_crop_height = int(width / aspect_ratio)
    else:  # Taller than wide (e.g., 3:4, 9:16)
        max_crop_height = height
        max_crop_width = int(height * aspect_ratio)

    # Ensure crop fits within image
    max_crop_width = min(max_crop_width, width)
    max_crop_height = min(max_crop_height, height)

    # Slider for crop width (height adjusts automatically)
    crop_width = st.slider("Crop width", 100, max_crop_width, min(300, max_crop_width))
    crop_height = int(crop_width / aspect_ratio)  # Lock height to ratio

    # Sliders for crop position
    left = st.slider("Left position", 0, width - crop_width, 0)
    top = st.slider("Top position", 0, height - crop_height, 0)

    if st.button('Crop Image'):
        with st.spinner('Cropping...'):
            # Crop the image
            right = left + crop_width
            bottom = top + crop_height
            
            # Validate crop boundaries
            right = min(right, width)
            bottom = min(bottom, height)
            crop_width = right - left
            crop_height = bottom - top
            
            cropped_img = image.crop((left, top, right, bottom))

            # Display the cropped image
            st.image(cropped_img, caption=f'Cropped Image ({selected_ratio_name})', use_column_width=True)

            # Convert to bytes for download
            img_bytes = io.BytesIO()
            cropped_img.save(img_bytes, format="PNG")
            img_bytes = img_bytes.getvalue()

            # Add download button
            st.download_button(
                label="Download Cropped Image",
                data=img_bytes,
                file_name=f"cropped_{selected_ratio_name.replace(':', 'x')}.png",
                mime="image/png"
            )
