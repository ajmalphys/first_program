''''''
import numpy as np

# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarr=arr.reshape(2,3,2)
# print(newarr)
# print(newarr.base) #[ 1 2 3 4 5 6 7 8 9 10 11 12]
#--------------------------------------------
'''unknown dimension'''

# arr=np.array([1,2,3,4,5,6,7,8])
# newarr=arr.reshape(2,2,-1)
# print(newarr.shape) # (2, 2, 2) assigned 2 for the unknown dimension
#---------------------------------------
'''flattening of arrays'''
# arr=np.array([[1,2,3],[4,5,6]])
# print(arr.reshape(-1)) #[1 2 3 4 5 6]










