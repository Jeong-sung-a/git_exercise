import numpy as np
import dlib
import cv2
import os, glob
import matplotlib.pyplot as plt

RIGHT_EYE = list(range(36, 42))
LEFT_EYE = list(range(42, 48))
EYES = list(range(36, 48))

frame_width = 640
frame_height = 480

face_classifier_frontal = cv2.CascadeClassifier("../FaceDetection/Resource/haarcascade_frontalface_default.xml")  # -- 본인 환경에 맞게 변경할 것


predictor_file = '../FaceDetection/Resource/shape_predictor_81_face_landmarks.dat'  # -- 본인 환경에 맞게 변경할 것
predictor = dlib.shape_predictor(predictor_file)

status = 'Awake'
min_EAR = 0.25
show_frame = None
color = None


def getEAR(points):
    A = np.linalg.norm(points[1] - points[5])
    B = np.linalg.norm(points[2] - points[4])
    C = np.linalg.norm(points[0] - points[3])
    return (A + B) / (2.0 * C)


def detectAndDisplay(image):
    global color
    global show_frame

    image = cv2.resize(image, (frame_width, frame_height))
    show_frame = image
    frame_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)
    faces = face_classifier_frontal.detectMultiScale(frame_gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        rect = dlib.rectangle(int(x), int(y), int(x + w),
                              int(y + h))
        points = np.matrix([[p.x, p.y] for p in predictor(image, rect).parts()])
        show_parts = points[EYES]
        right_eye_EAR = getEAR(points[RIGHT_EYE])
        left_eye_EAR = getEAR(points[LEFT_EYE])
        mean_eye_EAR = (right_eye_EAR + left_eye_EAR) / 2

        right_eye_center = np.mean(points[RIGHT_EYE], axis=0).astype("int")
        left_eye_center = np.mean(points[LEFT_EYE], axis=0).astype("int")

        cv2.putText(image, "{:.2f}".format(right_eye_EAR), (right_eye_center[0, 0], right_eye_center[0, 1] + 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        cv2.putText(image, "{:.2f}".format(left_eye_EAR), (left_eye_center[0, 0], left_eye_center[0, 1] + 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        for (i, point) in enumerate(show_parts):
            x = point[0, 0]
            y = point[0, 1]
            cv2.circle(image, (x, y), 1, (0, 255, 255), -1)

        if mean_eye_EAR > min_EAR:
            color = (0, 255, 0)
            status = 'Awake'
            print(status)
        else:
            color = (0, 0, 255)
            status = 'sleep'
            print(status)


base_dir = './faces'
dirs = [d for d in glob.glob(base_dir) if os.path.isdir(d)]
for dir in dirs:
    files = glob.glob(dir+'/*.jpg')
    print('\t path:%s, %dfiles'%(dir, len(files)))
    for file in files:
        print(file)
        image = cv2.imread(file)
        plt.imshow(image)
        plt.show()
        detectAndDisplay(image)