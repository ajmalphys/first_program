''''''
import numpy as np

# arr=np.array([1,2,3,4])
# print(arr.dtype) # int64
#-------------------------------
# arr=np.array(['a','b','c'])
# print(arr.dtype) # <U1
#-------------------------------
'''creating arrays with a defined data type'''

# arr=np.array([11,2,3,4],dtype='S')
# print(arr) # [b'11' b'2' b'3' b'4']
# print(arr.dtype) # |S2 2 represents the size of max value in the list

'''create an array with data type 4 bytes integer'''
# arr=np.array([1,2,3,4],dtype='i4')
# print(arr) # [1 2 3 4]
# print(arr.dtype) # int32

# arr=np.array(['a',2,3],dtype='i')
# print(arr) # throws back a value error
#---------------------------------------------------
# arr=np.array([-1.1,2.2,3.3,4.1])
# arr1=np.abs(arr)
# print(arr)
# print(arr1)
# arr2=arr1.astype('i')
# print(arr2)
#-------------------------------------------------------
'''change data type from integer to boolean'''
# arr=np.array([1,0,3])
# arr1=arr.astype('?')
# print(arr1)
# print(arr1.dtype)
#----------------------------------
# arr=np.array([1,2,3,4,5])
# x=arr.copy()
# arr[0]=40
# print(arr) # [40  2  3  4  5]
# print(x)  # [1 2 3 4 5]
#-----------------------------------
'''view()'''
# arr=np.array([1,2,3,4])
# x=arr.view()
# arr[0]=9
# print(arr) # [9 2 3 4]
# print(x) # [9 2 3 4]
#---------------------------------------
# arr=np.array([1,2,3,4])
# x=arr.view()
# x[0]=7
# print(arr) # [7 2 3 4]
# print(x) # [7 2 3 4]
#----------------------------------------
# arr=np.array([1,2,3,4,5])
# x=arr.copy()
# y=arr.view()
# print(x.base) # None
# print(y.base) # [1 2 3 4 5]