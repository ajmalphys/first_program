''''''
import numpy as np
#----------------------------
'''1D array'''
# arr=np.array([1,2,3])
# for x in arr:
#     print(x)
#----------------------------
'''2D array'''
# arr=np.array([[1,2,3],[4,5,6]])
# for x in arr:
#     print(x)
#--------------------------------
'''to get the scalar values'''
# arr=np.array([[1,2,3],[4,5,6]])
# for x in arr:
#     for y in x:
#         print(y)
#--------------------------------
'''iterating 3D arrays'''
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# for x in arr:
#   print(x)
#------------------------------------
'''iterating arrays using nditer()'''
# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# for x in np.nditer(arr):
#     print(x)
#-------------------------------------
