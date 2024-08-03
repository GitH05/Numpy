import numpy as np
arr = np.array([12,4,67,34,12,54])
print("\nArray:",arr)
print("cos value of the array:",np.cos(arr)) #used for graph representation

# minimum value
print("minimum value:",np.min(arr))
#  maximum value
print("maximum value:",np.max(arr))
#sum of the array
print("sum of the array:",np.sum(arr))

# iteration in array:
print("\nIteration in 1-D:")
for item in arr:
    print(item,end=" ")
print("\n")
# 2-D array
print("\nIteration in 2-D")
arr1 = np.array([[1,2,3,4],[5,6,7,8]])
for items in arr1:
    for eachItem in items:
        print(eachItem,end=" ")