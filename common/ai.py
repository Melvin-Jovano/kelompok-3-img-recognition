import numpy as np
import tensorflow as tf
import keras.utils as image
from keras.applications import VGG16

model = VGG16(weights='imagenet')

# Load and preprocess image
def preprocess(imgList):
    processedImg = []

    for i in imgList:
        img_path = f'img/{i}'
        img = image.load_img(img_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = tf.keras.applications.vgg16.preprocess_input(x)
        processedImg.append(x)

    return processedImg

# Predict image class
def predict(processedImg, imgList):
    preds = model.predict(np.vstack(processedImg))
    decode = tf.keras.applications.vgg16.decode_predictions(preds, top=3)
    result = []
    for i in range(len(processedImg)):
        predicted = {"Image" : f"img/{imgList[i]}", "Predicted" : decode[i]}
        print(f"Img : {predicted['Image']}\nPredicted : {predicted['Predicted']}")
        print("")
        result.append(predicted)
    return result