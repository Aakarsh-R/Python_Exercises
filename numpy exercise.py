lst = [5, 10, 0, 200]

lst = list(map(lambda x : x+5, lst))
print(lst)

#Using Numpy 
lst = [5, 10, 0, 200]

import numpy as np
arr = np.array(lst)

print(arr % 5)

#---------------------

lst = [1, 2, 3, 'text', True, 3+2j]
lst = list(map(lambda x : str(x), lst))
print(lst)

#Using Numpy 
lst = [1, 2, 3, 'text', True, 3+2j] 
import numpy as np
arr = np.array(lst)
print(type(arr[0]),type(arr[4]), type(arr[5]))


#---------------------

import sys
lst = [56, 45, 12, 6]
a = sys.getsizeof(max(lst))
print(a)

#Using Numpy 

lst = [56, 45, 12, 6]
import numpy as np
arr = np.array(lst)
print(arr.nbytes)


#--------------------------------------------------------------------------

import numpy as np

arr = np.array(['a',5.0,6,True,3+2j])
print(arr)
# [2 5 6 8]
print(type(arr))
# class 'numpy.ndarray'
print(np.result_type(arr))
# int32
print(type(arr[0]))

#---------------------

''' Creation of an array with step size 1.33 between 0 - 10 '''
print(np.arange(0, 10, 5, dtype = np.float64))
# [ 0.    1.33  2.66  3.99  5.32  6.65  7.98  9.31]
# arange() gives uncertain number of values based on steps
# Hence, we use linspace, which asks for total number of values 
''' Creation of an array with total 5 values between 0 - 160 '''
print(np.linspace(0, 160, 2, dtype = np.float64))
# [   0.   40.   80.  120.  160.] 


 
''' Method I: Using array and reshape to convert array into matrix '''
print(np.array([5,6,8,45,12,52]).reshape(3,2))
# [[ 5  6  8]
#  [45 12 52]]
''' Method II: Using matrix function '''
print(np.matrix([[1,2], [3,4], [5,6]]))
# [[1 2]
#  [3 4]]
''' Method III: Using misc. functions '''
print(np.eye(3, dtype = np.bool)) # Identity matrix
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]
print( np.zeros( (4,3), dtype = np.int ) )
# [[ 0.  0.  0.]
#  [ 0.  0.  0.]
#  [ 0.  0.  0.]
#  [ 0.  0.  0.]]
print(np.ones( (3,3), dtype = np.float ))
# [[ 1.  1.  1.]
#  [ 1.  1.  1.]
#  [ 1.  1.  1.]]
 

 