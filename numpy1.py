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

newarr = arr.reshape(2, 3, 2)
print(newarr)
