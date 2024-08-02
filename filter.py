import numpy as np
import basic as bs
print(bs.arr2)
arr2=bs.arr2
# filtering basic elements
print("Get specific element:",arr2[0,3])    #arr2[row,element-inddex]
# specific row:
print("Specific row:",arr2[0 :])    #arr2[row,:]
# print("escape:",arr2[1:3])
arr = np.array([1,2,4,6,2,6,32])

# slicing:
print("slice in 2-D:",arr2[1,0:3])  #arr2[row, start-index:end-index]


# start index: include  and  end index: exclude
print("Start to end-1:",arr[2:7])
# start to end:
print("start to end:",arr[0:])
# end to start
print("end to start:",arr[:-1])
# print(arr[-1])

# copy of an array:
arr4 = arr2.copy()
print("\nNew array:",arr4)
# matrix:
'''
Zero matrix:
'''
zeroMatrix = np.zeros((1,4,6))  #np.zeros(numberofmatrix,row,column)
print("\nZeroMatrix:",zeroMatrix)

'''other matrix:'''
print("\nOther matrix:",np.full((4,4),45))      #np.full((row,column),element)

'''decimal number matrix:'''
from numpy import random
x = random.randint(100)
print("\nRandom number:",x)

print("Random Matrix:",np.random.rand(4,4))


'''Identity Matrix:'''
print("\nIdentity Matrix:\n",np.identity(3))