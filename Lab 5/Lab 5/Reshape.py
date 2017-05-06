import numpy as np

a = np.arange(18)

a = a.reshape(3,3,2)

print("Number Dimention", a.ndim)
print("Datatype", a.dtype)
print("Shape" , a.shape)
print("Item Size", a.itemsize)
print("Size", a.size)
