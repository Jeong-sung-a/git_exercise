# import os
import cv2
import sys
import random
#
# # default 디렉터를 위한 HOG 객체 생성 및 설정
# hogdef = cv2.HOGDescriptor()
# hogdef.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
#
# # daimler 디텍터를 위한 HOG 객체 생성 및 설정
# hogdaim = cv2.HOGDescriptor((48, 96), (16, 16), (8, 8), 9)
# hogdaim.setSVMDetector(cv2.HOGDescriptor_getDaimlerPeopleDetector())
#
# cap = cv2.VideoCapture('../Show/Resource/Scene.mp4')
# mode = True    # 모드 변환을 위한 플래그 변수
# print('Toggle Space-bar to change mode.')
# while cap.isOpened():
#     ret, img = cap.read()
#     if ret:
#         if mode:
#             # default 디텍터로 보행자 검출
#             found, _ = hogdef.detectMultiScale(img)
#             for(x, y, w, h) in found:
#                 cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255))
#         else:
#             # daimler 디텍터로 보행자 검출
#             found, _ = hogdaim.detectMultiScale(img)
#             for(x, y, w, h) in found:
#                 cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0))
#         cv2.putText(img, 'Detector:%s'%('Default' if mode else 'Daimler'), (10, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 1)
#         cv2.imshow('frame', img)
#         key = cv2.waitKey(1)
#         if key == 27:
#             break
#         elif key == ord(' '):
#             mode = not mode
#     else:
#         break
# cap.release()
# cv2.destroyAllWindows()

# 동영상 불러오기
cap = cv2.VideoCapture('../MachineLearning/Resource/people_walking.mp4')

if not cap.isOpened():
    print('Video open failed!')
    sys.exit()

# 보행자 검출을 위한 HOG 기술자 설정
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # 매 프레임마다 보행자 검출
    detected, _ = hog.detectMultiScale(frame)  # 사각형 정보를 받아옴

    # 검출 결과 화면 표시
    for (x, y, w, h) in detected:
        c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv2.rectangle(frame, (x, y, w, h), c, 3)

    cv2.imshow('frame', frame)
    if cv2.waitKey(0) == 27:
        break

cv2.destroyAllWindows()