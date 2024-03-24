import numpy as np

a = np.arange(4).reshape(2, 2)
b = np.arange(10, 14).reshape(2, 2)

print(np.vstack((a, b)))    # 수직 병합
print(np.hstack((a, b)))    # 수평 병합
print(np.concatenate((a, b), 0))    # 수직 병합
print(np.concatenate((a, b), 1))    # 수평 병합

c = np.arange(12)
print(np.hsplit(c, 3))  # 배열을 3개로 쪼개기
print(np.hsplit(a, [3, 6]))    # [0:3], [3:6], [6:]

d = np.arange(12).reshape(4, 3)
print(np.vsplit(d, 2))
print(np.hsplit(d, [1]))    # [1:]로 쪼개기
