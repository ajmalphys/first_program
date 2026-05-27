''''''
import numpy as np

# a=np.array([1,2,3])
# b=np.array([3,4,5])
# c=np.concatenate((a,b))
# print(c)  # [1 2 3 3 4 5]
#-------------------------------


# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# a=np.stack((arr1,arr2),axis=1)
# print(a)
# b=np.hstack((arr1,arr2))
# print(b)
# c=np.vstack((arr1,arr2))
# print(c)
# d=np.dstack((arr1,arr2))
# print(d)

# arr=np.array([6,7,8,9,10])
# x=np.searchsorted(arr,100)
# print(x)
# print(arr)

arr=np.array([1,2,3,4,5,6,7])
filter_arr=arr%2==0
print(filter_arr)
new=arr[filter_arr]
print(new)