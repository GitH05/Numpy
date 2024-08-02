import numpy as np
# creating array
arr = np.array([23,6,1,0,6])
print(arr)

#  0 dimension array
arrZero = np.array(47)
print("\n0-D array:",arrZero)

# check dimension:
print("\nDimension of first::",arr.ndim)
print("\nDimension of second:",arrZero.ndim)

# 2-dimension array:
arr2 = np.array([[1,2,3,4,5],[1,2,3,4,7]])
print("\n2-D array:",arr2)
print("Dimension:",arr2.ndim)
# size
print("\nSize:",arr2.size)
# memory
print("memory:",arr2.nbytes)
# single element size:
print("single element size:",arr2.itemsize)
# check data type
print("DataType:",arr2.dtype)