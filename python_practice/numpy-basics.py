import numpy as np

#creating array 
array = np.array([1,2,3,4])
print(array.ndim)
print(type(array))

# basic array operations
array *= 2
print(array) 

# multi dimensional arrays

array_3d = np.array([[[1,2,3],[4,5,6],[7,8,9]],
                    [[1,2,3],[4,5,6],[7,8,9]],
                    [[1,2,3],[4,5,6],[7,8,9]]])
# accessing elements


number  = array_3d[0,1,0] +array_3d[1,0,2] + array_3d[2,1,1]
print(number)
