import numpy as np

#creating array 
array1 = np.array([1,2,3,4])
print(array1.ndim)
print(type(array1))

# basic array operations
array1 *= 2
print(array1) 

# multi dimensional arrays

array_3d = np.array([[[1,2,3],[4,5,6],[7,8,9]],
                    [[1,2,3],[4,5,6],[7,8,9]],
                    [[1,2,3],[4,5,6],[7,8,9]]])
# accessing elements
number  = array_3d[0,1,0] +array_3d[1,0,2] + array_3d[2,1,1]
print(number)

# slicing numpy array

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

# array[start:end:step]
#  accessing subset of array

print(array[:2,2:])

# for accessing individual rows and columns

print(array[0])

print(array[:,::-2])