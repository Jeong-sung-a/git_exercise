import numpy as np

a = np.array([1, 2, 3, 4])
print(a)
print(a.dtype) # 기본 int64
print(a.shape)

b = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(b)
print(b.shape)

c = np.array([1, 2, 3.14, 4])
print(c)
print(c.dtype) # 기본 float64

d = np.array([1, 2, 3, 4], dtype=np.float32)
print(d.dtype)

e = np.empty((2, 3)) # 초기화 되지 않은 쓰레기 값으로 배열 생성
print(e)
print(e.dtype)

e.fill(255) # 배열의 모든 요소를 value로 채움
print(e)

f = np.zeros((2, 3))
print(f)
print(f.dtype)

g = np.ones((2, 3))
print(g)