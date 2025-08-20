import numpy as np

# #creating array 
# array1 = np.array([1,2,3,4])
# print(array1.ndim)
# print(type(array1))

# # basic array operations
# array1 *= 2
# print(array1) 

# # multi dimensional arrays

# array_3d = np.array([[[1,2,3],[4,5,6],[7,8,9]],
#                     [[1,2,3],[4,5,6],[7,8,9]],
#                     [[1,2,3],[4,5,6],[7,8,9]]])
# # accessing elements
# number  = array_3d[0,1,0] +array_3d[1,0,2] + array_3d[2,1,1]
# print(number)

# # slicing numpy array

# array = np.array([[1,2,3,4],
#                   [5,6,7,8],
#                   [9,10,11,12],
#                   [13,14,15,16]])

# # array[start:end:step]
# #  accessing subset of array

# print(array[:2,2:])

# # for accessing individual rows and columns

# print(array[0])

# print(array[:,::-2])

# # scalar arithmetic

# array = np.array([1,2,3])

# print(array+1)
# print(array-2)
# print(array*3)
# print(array/4)
# print(array ** 5)

# #vectorized math funcs
# radii = np.array([1,2,3])

# ## area of circle 

# area = np.pi * radii**2
# print(area)

# # element wise arithmetic

# ar1 = np.array([2,4,6])
# ar2 = np.array([1,3,5])
# print(ar1 ** ar2)

# ## comparision operators

# scores = np.array([91,55,100,73,82,46])

# scores[scores < 60] = 0
# print(scores)

# # broadcast

# array2 = np.array([[1,2,3,4]])
# array3 = np.array([[1],[2],[3],[4]])

# print(array2.shape)
# print(array3.shape)

# ar = array3 * array2

# print(ar)

## handling missing values 

temperature = np.array([78,81,93,-999,65,-999,74,98]) # -999 = missing data

avg_temp = temperature[temperature != -999].mean()

clean_temp = np.where(temperature == -999,avg_temp, temperature)

print(clean_temp)