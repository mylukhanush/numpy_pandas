#creating array
# indexing
# slicing
# data types
#copy and view
#NumPy Array Shape
#Iterating

import numpy as np
# arr = np.array([1, 2, 3, 4])
# print(arr)
# x = np.zeros((2, 3))
# y = np.ones((2, 3))
# z = np.arange(0, 10, 2)
# a = np.linspace(0, 1, 5)
# print(x)
# print(y)
# print(z)
# print(a)

#Creating array for tuple
# arr = np.array((1, 3, 2))
# print(arr)

#Change data type from float to integer by using 'i'
# as parameter value:
# import numpy as np
# arr = np.array([1.1, 2.1, 3.1])
# newarr = arr.astype('i')
# print(newarr)

#copy and view
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# y = arr.view()
# print(x.base)
# print(y.base)

#Array Shape
# import numpy as np
# arr = np.array([[1, 2, 3],[4, 5, 6]])
# print(arr.shape)

#using funtion "ndmin"
# import numpy as np
# arr = np.array([1, 2, 3, 4, 7, 8], ndmin=6)
# print(arr)
# print('shape of array :', arr.shape)

#Reshape
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(4, 3)
# print(newarr)

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)

#Iterating
#Iterating means going through elements one by one.
#we can do this using basic for loop of python.
# import numpy as np
# arr = np.array([1, 2, 3])
# for x in arr:
#   print(x)

# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# for x in arr:
#   print(x)

# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# for x in arr:
#   for y in x:
#     print(y)

