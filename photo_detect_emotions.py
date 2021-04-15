from numpy.testing._private.utils import suppress_warnings
import streamlit as st

from PIL import Image
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.preprocessing import image as SImage
from keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from keras.models import model_from_json
DEMO_IMAGE = 'pexels-nappy-3460134.jpg'

classifier = model_from_json(open("facial_expression_model_structure.json", "r").read())
classifier.load_weights('facial_expression_model_weights.h5') #load weights

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
class_labels = ['Angry', 'Disgust', 'Dear', 'Happy', 'Sad', 'Surprise', 'Neutral']


@st.cache(ttl=3600, max_entries=10)
def detect_emotion(image):
    # redimensionnement de la frame
    frame = image

    labels = []
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

        if np.sum([roi_gray]) != 0:
            roi = roi_gray.astype('float') / 255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)

            preds = classifier.predict(roi)[0]
            label = class_labels[preds.argmax()]

            label_position = (x, y)
            cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 3)
        else:
            cv2.putText(frame, 'pas de visage trouvé', (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 2)

    return frame


st.title("Application de détection d'émotion")

st.markdown('''
            Ce modèle détecte les émotions d'une image
            ''')

img_file_buffer = st.file_uploader("Upload an image", type=["jpg", "jpeg", 'png'])

if img_file_buffer is not None:
    image = np.array(Image.open(img_file_buffer))

else:
    demo_image = DEMO_IMAGE
    image = np.array(Image.open(demo_image))

st.subheader('Original Image')

st.image(image, caption=f"Original Image", use_column_width=True)

emotion_analysis = detect_emotion(image)
st.markdown('''
            Ce modèle détecte la colère, la joie, le neutre , la surprise, la tristesse, le dégoût et la peur.
            ''')

st.subheader('Analyse des émotions')

st.image(emotion_analysis, caption=f"Image détectée", use_column_width=True)


