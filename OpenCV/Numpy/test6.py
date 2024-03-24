import numpy as np

a = np.arange(10, 20)
print(np.where(a > 15))    # 조건에 맞는 인덱스 출력
print(np.where(a > 15), 1, 0)   # 조건에 맞으면 1, 아니면 0
print(np.where(a > 15), a, 0)   # 조건에 맞으면 a, 아니면 0

z = np.array([0, 1, 2, 0, 1, 2])
print(np.nonzero(z))    # 0이 아닌 요소의 인덱스를 배열로 만들어 반환

t = np.array([True, True, True])
print(np.all(t))
t[1] = False
print(np.all(t))

tt = np.array([[True, True], [False, True], [True, True]])
print(np.all(tt, 0)) # 수직 비교
print(np.all(tt, 1)) # 수평 비교

a = np.arange(10)
b = np.arange(10)
print(a == b)
print(np.all(a == b))
b[5] = -1
print(a == b)
print(np.all(a == b))
