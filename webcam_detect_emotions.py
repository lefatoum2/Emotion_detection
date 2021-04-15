import streamlit as st
import numpy as np
import cv2
from keras.preprocessing.image import img_to_array
from keras.models import model_from_json


st.title("Detecteur d'émotion")
run = st.checkbox('Démarrage')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)


classifier = model_from_json(open("facial_expression_model_structure.json", "r").read())
classifier.load_weights('facial_expression_model_weights.h5') #load weights

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
class_labels = ['Angry', 'Disgust', 'Dear', 'Happy', 'Sad', 'Surprise', 'Neutral']


@st.cache(ttl=3600, max_entries=10)
def detect_emotion(image):
    # resize the frame to process it quickly
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
            cv2.putText(frame, 'Pas de visage trouvé', (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 2)

    return frame


while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    ana = detect_emotion(frame)
    FRAME_WINDOW.image(ana)
else:
    st.write('Arrêté')