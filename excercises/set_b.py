''''''
'''Qn : 1
Write a Python script to find all Armstrong numbers in the range from 1 to 10000 
and add them to a list. Then, calculate the sum and the average of these Armstrong numbers. 
Additionally, determine and print the smallest and largest Armstrong numbers within this range.'''

# l=[]
# for i in range(1,10001):#153
#     s=0
#     f=i
#     k=len(str(f))#3
#     while f>0: #153--15--1
#         j=f%10 #3--5--1
#         s+=(j**k) #3**3--5**3--1**3
#         f//=10 #15--1--0
#     if s==i:
#         l.append(i)
# print(l)
# print(f'Sum of the armstrons numbers in this range is : {sum(l)}')
# print(f'Average of the armstrong numbers in the list is : {(sum(l)/len(l))}')
# print(f'Smallest armstrong number is :{min(l)}')
# print(f'largest armstron number in the range is : {max(l)}')

'''---output---'''
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474]
# Sum of the armstrons numbers in this range is : 20662
# Average of the armstrong numbers in the list is : 1291.375
# Smallest armstrong number is :1
# largest armstron number in the range is : 9474

'''Qn:2
Write a Python script to find the second smallest number in a given list of integers.
 Then, perform the following tasks:

    Remove all occurrences of the second smallest number from the list.

    Calculate the product of the remaining numbers in the list.

    Sort the modified list in descending order and print it.'''

# l=[1,2,2,3,4,5,6,7,8,9]
# l.remove(min(l))
# print(l)
# print(f'The second smallest number in the list is : {min(l)}')
# #removing all the duplicates
# s=set(l)
# l2=list(s)
# print(f'removing the duplicates : {l2}')
# product=1
# for i in l2:
#     product*=i
# print(f'product of elements in the list {l2} is : {product}')
# l2.sort(reverse=True)
# print(f'Printing the final list in descending order : {l2}')
'''---output---'''
# [2, 2, 3, 4, 5, 6, 7, 8, 9]
# The second smallest number in the list is : 2
# removing the duplicates : [2, 3, 4, 5, 6, 7, 8, 9]
# product of elements in the list [2, 3, 4, 5, 6, 7, 8, 9] is : 362880
# Printing the final list in descending order : [9, 8, 7, 6, 5, 4, 3, 2]

''''Qn:3

Write a Python script using list comprehension to perform the following tasks on a given list of integers:
numbers = [4, 9, 12, 15, 22, 30, 36, 45, 50]
1--Create a new list containing all integers from the original list that are both divisible by 3 and 
   greater than 10.
2--Create another list containing the square root of each number from the filtered list.
3--Filter this new list to keep only those values that are greater than 5.
4--Print the final filtered list of square roots.'''

# numbers = [4, 9, 12, 15, 22, 30, 36, 45, 50]
# list_1=[x for x in numbers if (x%3==0) & (x>10)]
# print(list_1)
# list_2=[x**(1/2) for x in list_1]
# print(list_2)
# list_3=[x for x in list_2 if x>5]
# print(list_3)
'''---output---'''
# [12, 15, 30, 36, 45]
# [3.4641016151377544, 3.872983346207417, 5.477225575051661, 6.0, 6.708203932499369]
# [5.477225575051661, 6.0, 6.708203932499369]

