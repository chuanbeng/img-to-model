import numpy as np
import tensorflow as tf
from tensorflow import keras
import io
import streamlit as st
from PIL import Image
from tempfile import NamedTemporaryFile
import pandas as pd

st.set_option('deprecation.showfileUploaderEncoding', False)

model = tf.keras.models.load_model('tfbase.h5') #simple model
#model = tf.keras.models.load_model('tfaug.h5') #augmented model

#===================
#define image height and width
#import class_names
#===================
img_height = 180
img_width = 180
class_names = np.load('class_names.npy')
#st.write(class_names)

def saveImage(byteImage):
    bytesImg = io.BytesIO(byteImage)
    imgFile = Image.open(bytesImg)   
    return imgFile

st.write("""
         # Model Prediction Demo
         """
         )
#st.write("This is a simple image classification web app to predict model of converter")
fileUpload = st.file_uploader("Upload a JPG or PNG image file", type=["jpg", "png", "jpeg"])
temp_file = NamedTemporaryFile(delete=False)

if fileUpload is None:
    st.text("To begin, please upload an image file")
else:

    file = fileUpload.read()
    path = saveImage(file)
    st.write(path)
    st.image(path, use_column_width=True)
    temp_file.write(fileUpload.getvalue())
    img = tf.keras.utils.load_img(temp_file.name, target_size=(img_height, img_width))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    st.write(
        "This image most likely belongs to model ID no. {} with a {:.2f} percent confidence."
        .format(class_names[np.argmax(score)], 100 * np.max(score))
    )
    st.write("Showing list of IDs with probabilities > 10%")
    list_prob = score.numpy()
    list_class = class_names
    joined_list = list(zip(list_class, list_prob))
    joined_df = pd.DataFrame(joined_list, columns=["id","p"])
    joined_df_sorted = joined_df.sort_values(by=["p"], ascending=False)
    joined_df_filtered = joined_df_sorted[joined_df_sorted["p"] > 0.1]
    st.write(joined_df_filtered)

