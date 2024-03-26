import cv2
import numpy as np

img = cv2.imread('../ImageProcessing/Resource/clock.jpg')

x = 320; y = 150; w = 50; h = 50    # roi 좌표
roi = img[y:y+h, x:x+w]     # roi 지정

print(roi.shape)
cv2.rectangle(roi, (0, 0), (h-1, w-1), (0, 255, 0)) # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0)) => 한 번에 작성
cv2.imshow("img", img)                              # 선을 그리기 위해 1픽셀을 뺐다.

cv2.waitKey(0)
cv2.destroyAllWindows()