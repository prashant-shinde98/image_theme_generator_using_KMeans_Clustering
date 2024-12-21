# Streamlit App
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image, ImageDraw

st.title("Image Theme Generator")
st.write("Upload an image to generate a theme based on its colors.")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    image = np.array(image)


    X = image.reshape(-1,3)

    from sklearn.cluster import KMeans

    kmeans = KMeans(n_clusters=3)
    kmeans.fit(X)

    res = kmeans.cluster_centers_

    def create_color_palatte(dominant_colors, palatte_size = (300,50)):
        #create image to display colors
        palatte = Image.new("RGB", palatte_size)
        draw = ImageDraw.Draw(palatte)

        #calculate width of each color swatch
        swatch_width = palatte_size[0] //  len(dominant_colors)
        #draw each color as rectangle in a palatte
        for i, color in enumerate(dominant_colors):
            draw.rectangle([i * swatch_width, 0, (i + 1) * swatch_width, palatte_size[1]], fill= tuple(color))

        return palatte
    

    theme = create_color_palatte(res.astype(int))



    # Generate and display the theme
    st.write("## Generated Theme")
    st.image(theme, caption="Generated Theme", use_column_width=True)