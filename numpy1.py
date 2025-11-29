import numpy as np

print(np.__version__)

#---------------------------------------------#

# Array

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arr1 = np.array(["archer","wood","atkinson",'carse',"stokes"])

print(arr)
print(arr1)

#===================================================#

import numpy as np

arr = np.array(42)
print(arr)

# 2d Array

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# 3d Array

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)

#

import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Higher Dimensional Array

import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)

# Array Access Elements :

import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr[3])          # prints element at index 3 → 4
print(arr[1] + arr[3]) # prints 2 + 4 → 6

# 2d Array Accessing 

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])
print('2nd element on 1st row: ', arr[1, 3])

# 3d Array Excess

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], 
                [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])   # 6
print(arr[1, 1, 2])   # 12

# Negative Indexing 

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])

# Slicing Array

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])
print(arr[3:6])

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])
print(arr[:6])

# Negative Slicing Array

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])
print(arr[-2:0])

#step Slicing array

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])

# slicing 2d Array

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])
print(arr[0, 1:4])
#-------------------------------------------------#

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])
print(arr[0:2, 1:4])

# checking the Data Type

import numpy as np

arr = np.array([1, 2, 3, 4])
arr2 = np.array(["kaushik","ruke"])

print(arr.dtype)
print(arr2.dtype)

#-------------------------------------------------#

import numpy as np

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

#-------------------------------------#

import numpy as np

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)

#--------------------------------------------------#

import numpy as np

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)

#------------------------------------------------------------#

import numpy as np

arr = np.array(['a', '2', '3'], dtype='object')

#--------------------------------------------------------------------#

import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)

#---------------------------------------------------------------------#

import numpy as np

arr = np.array ([1,0,3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)

#-------------------------------------------------------------------#

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

#----------------------------------------------------------------------#

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)

#-------------------------------------#

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

#-------------------------------------------------------------#

import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)

#----------------------------------------------------------------#

# RESHAPE

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

#1d to 2d

newarr = arr.reshape(4, 3)  # 4 Rows and 3 columns
print(newarr)

#----------------------------------------------#

# 1d to 3d

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)  # 2 Columns, 3 Rows and 2 Arrays
print(newarr)

#------------------------------------#

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base) # will Return as it is for OUTPUT

#----------------------------------------------------#

# Convert into 1d Array

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)
print(newarr)


# Iterating 1d Array

import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
  print(x)
  
  
# Iterating as 2d Array

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)


# iterating 2d arrays on different scalar element.

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)


# Iterating 3d arrays 

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)


# iterating 3d arrays on different scalar element, Iterate Each Dimension 

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)


# Iterating Array using nditer()

import numpy as np 

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)


# Iterate Array using Different Data Types :

import numpy as np

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)
  
  
  
# Iterating with Different Step Size 

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)

#Enumerated Iteration Using ndenumerate()

import numpy as np

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)
  
# Enumerate on following 2D array's elements:

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)


# Joining Numpy Arrays :

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))

print(arr)


# Joining 2d arrays as along Axis :

import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)

print(arr)


# Joining Arrays Using Full stack Function

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)

print(arr)


# Array Splitting

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])

#----------------------------------------------------------#

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)
print(newarr)


# arrays Search 

import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)
print(x)

#------------------# 

import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')
print(x)

#-----------------------------------------------#

import numpy as np

arr = np.array([3, 2, 0, 1])
print(np.sort(arr))
