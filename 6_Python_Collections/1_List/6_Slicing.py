''''''

'''need to create a list from an existing list'''

# lst=[3,4,5,6,7,1,2,3,9,10,11,34]
# #--- 0,1,2,3,4,5,6,7,8,9,10,11,12  index values of lst
# lst2=lst[2:5]   #---use square brackets
# print(lst2) #---[5, 6, 7]

'''syntax of slicing----[initial index : final index : step size'''
''' the element corresponding to final index is not included(similar to the working of range)'''

# lst=[3,4,5,6,7,1,2,3,9,10,11,34]
# print(lst[0:5:2]) #-------[3, 5, 7]
# print(lst[3:4]) #---------[6]
# print(lst[0:12]) #--------[3, 4, 5, 6, 7, 1, 2, 3, 9, 10, 11, 34]
# print(lst[0:12:3]) #------[3, 6, 2, 10]
# print(lst[:4]) #----------[3, 4, 5, 6]---list till index 4 from index=0
# print(lst[4:]) #----------[7, 1, 2, 3, 9, 10, 11, 34]---list till end from index 4
# print(lst[:]) #-----------[3, 4, 5, 6, 7, 1, 2, 3, 9, 10, 11, 34]---full list
# print(lst[::2]) #---------[3, 5, 7, 2, 9, 11]------full list with a step size of 2
# print(lst[::5]) #---------[3, 1, 11]
# print(lst[::-1]) #--------[34, 11, 10, 9, 3, 2, 1, 7, 6, 5, 4, 3]-----reversing



'''Qn:1 wap to check a given string is palindrome or not'''

# a='malayalam'
# # print(a[::-1])
# if a==a[::-1]:
#     print('Palindrome')
# else:
#     print('Not palindrome')
# #output: palindrome

# a=input('Enter a word: ')
# # print(a[::-1])
# if a==a[::-1]:
#     print('Palindrome')
# else:
#     print('Not palindrome')
# #output: palindrome

