import cv2

img_file = "../Show1/Resource/girl.jpg" # 표시할 이미지 경로(./../현재 디렉토리/sample2.xlsx)
img = cv2.imread(img_file) # 이미지를 읽어서 img 변수에 할당

if img is not None:
    cv2.imshow('IMG', img) # 읽은 이미지를 화면에 표시
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows() # 키 q가 입력될 때까지 대기 & 창 모두 닫기
else:
    print('No image file')
