import cv2

# 얼굴 검출을 위한 캐스케이드 분류기 생성
face_cascade = cv2.CascadeClassifier('../MachineLearning/Resource/haarcascade_frontalface_default.xml')
# 눈 검출을 위한 캐스케이드 분류기 생성
eye_cascade = cv2.CascadeClassifier('../MachineLearning/Resource/haarcascade_eye.xml')

# 카메라 캡처 활성화
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, img = cap.read()   # 프레임 읽기
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 얼굴 검출
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(80, 80))
        # 검출된 얼굴 순회
        for(x, y, w, h) in faces:
            # 검출된 얼굴에 사각형 표시
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            # 얼굴 영역을 ROI로 설정
            roi = gray[y:y+h, x:x+w]
            # ROI에서 눈 검출
            eyes = eye_cascade.detectMultiScale(roi)
            # 검출된 눈에 사각형 표시
            for i, (ex, ey, ew, eh) in enumerate(eyes):
                if i >= 2:
                    break
                cv2.rectangle(img[y:y+h, x:x+w], (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        # 결과 출력
        cv2.imshow('face detect', img)
    else:
        break
    if cv2.waitKey(5) == 27:
        break
cv2.destroyAllWindows()

