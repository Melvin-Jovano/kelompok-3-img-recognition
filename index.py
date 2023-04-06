# !pip install tensorflow
# !pip install numpy

import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import VGG16

# Load pre-trained VGG16 model
model = VGG16(weights='imagenet')

# Load and preprocess image
img_path = 'img/cat_1.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = tf.keras.applications.vgg16.preprocess_input(x)

# Predict image class
preds = model.predict(x)
print('Predicted:', tf.keras.applications.vgg16.decode_predictions(preds, top=3)[0])

# Output: 
# array of: (class_indentifier, object_prediction, confidence_level)