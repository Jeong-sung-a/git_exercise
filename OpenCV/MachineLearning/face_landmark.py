import cv2
import dlib

# # 얼굴 검출기와 랜드마크 검출기 생성
# detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor('../MachineLearning/Resource/shape_predictor_81_face_landmarks.dat')
#
# img = cv2.imread("../MachineLearning/Resource/front_face.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # 얼굴 영역 검출
# faces = detector(gray)
# for rect in faces:
#     # 얼굴 영역을 좌표로 변환한 후 사각형 표시
#     x, y = rect.left(), rect.top()
#     w, h = rect.right()-x, rect.bottom()-y
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
#
#     # 얼굴 랜드마크 검출
#     shape = predictor(gray, rect)
#     for i in range(68):
#         # 부위별 좌표 추출 및 표시
#         part = shape.part(1)
#         cv2.circle(img, (part.x, part.y), 2, (0, 0, 255), -1)
#         cv2.putText(img, str(i), (part.x, part.y), cv2.FONT_HERSHEY_PLAIN, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
#
# cv2.imshow("face landmark", img)
# cv2.waitKey(0)

import numpy as np
import dlib
import cv2

RIGHT_EYE = list(range(36, 42))
LEFT_EYE = list(range(42, 48))
MOUTH = list(range(48, 68))
NOSE = list(range(27, 36))
EYEBROWS = list(range(17, 27))
JAWLINE = list(range(1, 17))
ALL = list(range(0, 68))
EYES = list(range(36, 48))


#-- 데이터 파일과 이미지 파일 경로
predictor_file = '../MachineLearning/Resource/shape_predictor_81_face_landmarks.dat' #-- 자신의 개발 환경에 맞게 변경할 것
image_file = '../MachineLearning/Resource/front_face.jpg' #-- 자신의 개발 환경에 맞게 변경할 것

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_file)

image = cv2.imread(image_file)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

rects = detector(gray, 1)
print("Number of faces detected: {}".format(len(rects)))


for (i, rect) in enumerate(rects):
    points = np.matrix([[p.x, p.y] for p in predictor(gray, rect).parts()])
    show_parts = points[ALL]
    for (i, point) in enumerate(show_parts):
        x = point[0,0]
        y = point[0,1]
        cv2.circle(image, (x, y), 1, (0, 255, 255), -1)
        cv2.putText(image, "{}".format(i + 1), (x, y - 2),
		cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1)

cv2.imshow("Face Landmark", image)
cv2.waitKey(0)