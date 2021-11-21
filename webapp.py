import numpy as np
import tensorflow as tf
import io
import streamlit as st
from PIL import Image
from tempfile import NamedTemporaryFile


st.set_option('deprecation.showfileUploaderEncoding', False)
model = tf.keras.models.load_model('tfbase.h5') #simple model

st.write("""
         # Model Prediction
         """
         )
#st.write("This is a simple image classification web app to predict model of converter")
fileUpload = st.file_uploader("Upload a JPG or PNG image file", type=["jpg", "png", "jpeg"])

if fileUpload is None:
    st.text("To begin, please upload an image file")
else:
    file = fileUpload.read()
    path = saveImage(file)
    st.write(path)
    st.image(path, use_column_width=True)
