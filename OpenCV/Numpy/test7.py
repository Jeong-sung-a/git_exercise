import numpy as np

a = np.arange(12).reshape(3, 4)
print(np.sum(a))
print(np.sum(a, 0))    # 수직
print(np.sum(a, 1))    # 수평

'''
mean = 평균
amin = 최소 값
amax = 최대 값
'''