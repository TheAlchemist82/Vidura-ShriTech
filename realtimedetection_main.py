import cv2
from keras.models import model_from_json
import numpy as np
from datetime import datetime
from os import path

BASE_DIR = './videos'
PREFIX = 'footage'
EXTENSION = 'mp4'
file_name_format = "{:s}-{:d}-{:%Y%m%d_%H%M%S}.{:s}"

date = datetime.now()
not_detected_posture = 0
file_name = file_name_format.format(PREFIX, not_detected_posture, date, EXTENSION)
file_path = path.normpath(path.join(BASE_DIR, file_name))


json_file = open("emotiondetector.json", "r")
model_json = json_file.read()
json_file.close()
model = model_from_json(model_json)

model.load_weights("emotiondetector.h5")
haar_file=cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade=cv2.CascadeClassifier(haar_file)

def extract_features(image):
    feature = np.array(image)
    feature = feature.reshape(1,48,48,1)
    return feature/255.0


writer= cv2.VideoWriter(file_path, cv2.VideoWriter_fourcc(*'MP4V'), 20.0, (640, 480))
webcam=cv2.VideoCapture(0)
labels = {0 : 'angry', 1 : 'disgust', 2 : 'fear', 3 : 'happy', 4 : 'neutral', 5 : 'sad', 6 : 'surprise'}
while True:
    i,im=webcam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(im,1.3,5)
    try: 
        for (p,q,r,s) in faces:
            image = gray[q:q+s,p:p+r]
            cv2.rectangle(im,(p,q),(p+r,q+s),(255,0,0),2)
            image = cv2.resize(image,(48,48))
            img = extract_features(image)
            pred = model.predict(img)
            prediction_label = labels[pred.argmax()]
            # print("Predicted Output:", prediction_label)
            # cv2.putText(im,prediction_label)
            cv2.putText(im, '% s' %(prediction_label), (p-10, q-10),cv2.FONT_HERSHEY_COMPLEX_SMALL,2, (0,0,255))
        cv2.imshow("Output",im)
        cv2.waitKey(27)
        writer.write(im)

    except cv2.error:
        pass
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break
    