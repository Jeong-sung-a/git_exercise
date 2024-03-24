import numpy as np

a = np.arange(5)
print(a)  # 순차적인 값으로 생성
print(a.dtype)  # int64 기본값
print(a.shape)

b = np.arange(5.0)  # 명시적으로 float64 지정
print(b)
print(b.dtype)

c = np.arange(3, 9, 2)  # 3에서 8까지 2씩 증가하는 배열
print(c)

d = np.arange(5)
print(d)
print(d.dtype)

e = d.astype('float32')
print(e)
print(e.dtype)

f = np.arange(6)
g = f.reshape(2, 3)
print(g)
h = np.reshape(f, (2, 3))
print(h)

i = np.arange(100).reshape(-1, 5)  # 해당 차수에 대해 크기를 지정 X
print(i)
print(i.shape)

j = np.zeros((2, 3))
print(j)
print(j.reshape((6,)))
print(j.reshape(-1))
print(np.ravel(j))
