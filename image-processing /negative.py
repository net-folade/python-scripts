'''
The app allows users to upload an image, processes it to create a negative (inverted colors), 
and provides an option to download the resulting image.
'''

import streamlit as st
from PIL import Image
import numpy as np
import io

# Streamlit UI
st.title('Negative Image Generator')
st.write('Upload an image to create its negative (inverted colors)!')

# Upload image
uploaded_img = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_img is not None:
    # Open and display the original image
    image = Image.open(uploaded_img).convert('RGB')  # Ensure RGB format
    st.image(image, caption='Original Image', use_column_width=True)

    if st.button('Create Negative'):
        with st.spinner('Processing...'):
            # Convert image to NumPy array
            img_array = np.array(image)
            
            # Invert colors (255 - each RGB value)
            negative_array = 255 - img_array
            
            # Convert back to PIL Image
            negative_img = Image.fromarray(negative_array)

            # Display the negative image
            st.image(negative_img, caption='Negative Image', use_column_width=True)

            # Convert to bytes for download
            img_bytes = io.BytesIO()
            negative_img.save(img_bytes, format="PNG")
            img_bytes = img_bytes.getvalue()

            # Add download button
            st.download_button(
                label="Download Negative Image",
                data=img_bytes,
                file_name="negative_image.png",
                mime="image/png"
            )