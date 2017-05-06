import numpy as np

a=np.zeros((4,5))
print("Zeros", a)

b=np.ones((3,4))
print("Ones",b )

b=np.ones((3,3))
b= b*6
print("Six", b)

b= np.linspace(0,2,9)
print("Linspace", b)


c=np.sin(b)
print("Sin", c)

c=np.cos(b)
print("Cos", b)

