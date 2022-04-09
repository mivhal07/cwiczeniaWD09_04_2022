import numpy as np

a = np.array([1, 2, 3], dtype='float64')
print(a)
a = np.arange(1, 5, 0.5)
print(a)
print(a.dtype)
print(type(a))
print(a.shape)
print(a.ndim)

b = np.array([np.arange(2), np.arange(2)])
print(b)
print(b.ndim)
print(b.shape)

