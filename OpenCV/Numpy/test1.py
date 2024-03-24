'''
ndim : 차원(축)의 수
shape : 각 차원의 크기(튜플)
size : 전체 요소의 개수, shape의 각 항목의 곱
dtype : 요소의 데이터 타입
itemsize : 각 요소의 바이트 크기
'''

import cv2
img = cv2.imread("../Show1/Resource/girl.jpg")
print(type(img))
print(img.ndim)     # 3차원 배열
print(img.shape)    # 행x열x채널(높이x폭x3)
print(img.size)     # 각 차원의 길이 곱한 값
print(img.dtype)
print(img.itemsize)