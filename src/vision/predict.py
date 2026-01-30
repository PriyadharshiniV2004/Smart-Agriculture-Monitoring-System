import tensorflow as tf
import numpy as np
import cv2
from keras.models import load_model
from vision.class_labels import TOMATO_CLASSES, PEST_CLASSES
from vision.preprocess import preprocess_image

tomato_model = load_model("models/tomato_disease_model.h5")
pest_model = load_model("models/pest_detection_model.h5")

def predict_image(img, model_type="tomato"):
    img = preprocess_image(img)
    img = cv2.resize(img, (256, 256))
    img = tf.keras.preprocessing.image.img_to_array(img)
    img = np.expand_dims(img, axis=0)

    if model_type == "tomato":
        model = tomato_model
        classes = TOMATO_CLASSES
    else:
        model = pest_model
        classes = PEST_CLASSES

    predictions = model.predict(img)
    index = np.argmax(predictions[0])

    return classes[index], round(100 * predictions[0][index], 2)
