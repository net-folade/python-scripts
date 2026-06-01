'''
Streamlit app to split an uploaded image into a grid and allow users to download each piece.
'''

import streamlit as st
from PIL import Image
import numpy as np
import io

# Streamlit UI
st.title('Image Splitter')
st.write('Upload an image and choose how to split it into a grid!')

# Upload image 
uploaded_img = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_img is not None:
    # Open and display the original image
    image = Image.open(uploaded_img).convert('RGB')  # Convert to RGB for consistency
    st.image(image, caption='Original Image', use_column_width=True)

    # Let user choose grid size
    grid_size = st.slider("Choose grid size (e.g., 3 means 3x3)", min_value=2, max_value=6, value=3)

    if st.button('Split Image'):
        with st.spinner('Splitting...'):
            # Convert image to NumPy array for easier manipulation
            img_array = np.array(image)
            height, width = img_array.shape[:2]
            # Calculate size of each grid section
            section_height = height // grid_size
            section_width = width // grid_size

            # List to store grid pieces 
            grid_pieces = []  

            # Split the image into grid sections
            for i in range(grid_size):
                for j in range(grid_size):
                    # Crop the image using array slicing
                    piece = img_array[
                        i * section_height:(i + 1) * section_height,
                        j * section_width:(j + 1) * section_width
                    ]
                    # Convert back to PIL Image
                    piece_img = Image.fromarray(piece)
                    grid_pieces.append(piece_img)

            # Display the grid pieces
            st.write(f"Image split into {grid_size}x{grid_size} grid:")
            cols = st.columns(grid_size)  # Create columns for layout
            piece_index = 0
            for i in range(grid_size):
                for j in range(grid_size): 
                    with cols[j]:
                        # display the image
                        st.image(grid_pieces[piece_index], use_column_width=True)


                        # Convert image to bytes for download
                        img_bytes = io.BytesIO()
                        grid_pieces[piece_index].save(img_bytes, format="PNG")
                        img_bytes = img_bytes.getvalue()

                        # Add download button
                        st.download_button(
                            label=f"Download Piece {piece_index + 1}",
                            data=img_bytes,
                            file_name=f"piece_{piece_index + 1}.png",
                            mime="image/png"
                        )
                    piece_index += 1

