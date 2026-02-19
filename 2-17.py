import numpy as np


z = np.arange(10)
print(z)
z = np.arange(5, 100, 20)
print(z)
z = np.linspace(-5.2,10.9,5)
print(z)


a = np.array([1, 2 , 3 , 4])

print(a)
print(a.shape)
print(len(a))
print(a.size)
print(a.ndim)

print("a:", a)

a = np.array([[1,2], [3,4], [5,6]])
print(a)
b = a.reshape (2,3)
print(b)
c = a.reshape(2,-1)
print(c)

print
