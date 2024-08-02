import numpy as np
arrm = np.array([21,54,9,21,6,32])
print("\n1-D:",arrm)
# plus operation
print("\naddition with each array element:")
arrm = arrm + 10
print(arrm)

#subtraction operation
arrm = arrm -11
print("\nsubtraction with each array elements:",arrm)

#multiplication operation:
arrm = arrm * 10
print("\nMultiplication with each array elements:",arrm)

#Division operation:
arrm = arrm / 11
print("\nDivision with each array elements:",arrm)

# operation between two array:
arrm1 = np.array([21,54,65,2,7,5])
print("\nSecond array:",arrm1)
#mathematical operation between two array:
print("\narray-1:",arrm)
print("array-2:",arrm1)
print("\nAddition between two array:",(arrm + arrm1))
print("\nSubtraction between two array:",(arrm - arrm1))
print("\nMultiplication between two array:",(arrm * arrm1))
print("\nDivision between two array:",(arrm / arrm1))