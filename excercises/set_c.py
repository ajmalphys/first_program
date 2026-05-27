''''''
'''
Qn:1--Write a Python script to find all perfect numbers in the range from 1 to 10000 
and add them to a list. Then, calculate the sum and the average of these perfect numbers. 
Additionally, determine and print the smallest and largest perfect numbers within this range.'''

#perfect number : sum of divisors except that number is that number
# l=[]
# for i in range(3,10001):
#     s=0
#     for j in range(1,(i//2)+1):
#         if i%j==0:
#             s+=j
#         else:
#             pass
#     if s==i:
#         l.append(i)
# print(l) #[6, 28, 496, 8128]
# print(f'The sum of the given perfect numbers are : {sum(l)}')
# print(f'Average of the given nos are : {sum(l)/len(l)}')
# print(f'minimum value is : {min(l)}')
# print(f'maximum value is : {max(l)}')
'''---output---'''
# [6, 28, 496, 8128]
# The sum of the given perfect numbers are : 8658
# Average of the given nos are : 2164.5
# minimum value is : 6
# maximum value is : 8128

'''
Qn : 2--Write a Python script to find the second smallest even number in a given list of integers. 
Then, perform the following tasks:
Remove all occurrences of the second smallest even number from the list.
Calculate the sum of the remaining numbers in the list.
Sort the modified list in ascending order and print it.'''

# l=[1,2,3,4,5,7,2,4,6]
# unique=list(set(l)) #removed all occurences of the second smallest even number
# print(unique)
# print(sum(unique)) #printing the sum of remaining numbers
# unique.sort() #sorts the unique list in ascending order. sort() is an inplace modifier
# print(unique)
'''-----output-----'''
# [1, 2, 3, 4, 5, 6, 7]
# 28
# [1, 2, 3, 4, 5, 6, 7]

'''Qn:3
Write a Python script using 'list comprehension' to perform the following tasks on a given list of strings:  

Create a new list containing the length of each string in the original list if the string 
contains the letter 'e' and its length is greater than 3.  
Create another list containing the square of each length from the first list.  
Filter this second list to keep only values that are even.  
Print the final list of squares that are even.  
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]'''


# list_1=["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
# #list containing the length of each string in list_1
# list_2=[len(x) for x in list_1 if (('e' in x) and (len(x)>3))]
# print(list_2)
# #list containing the square of each length from list_1
# list_3=[(len(x)**2) for x in list_1]
# print(list_3)
# #filter list_3 to keep even nos only
# list_4=[x for x in list_3 if x%2==0]
# print(list_4)
'''---output---'''
# [5, 6, 4, 10, 5]
# [25, 36, 36, 16, 100, 9, 25]
# [36, 36, 16, 100]




