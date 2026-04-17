#descions are made based on a condition

# age=18
# print('you can vote')
# print('you cant vote')

#three types are there
#if, if else, if elif else
#-----------------------------------------------------------------------------------
'''SIMPLE IF'''
#Syntax of IF
# if condition: #Block statement
#     statement #need to maintain a space called indent
#-----------------------------------------------------------------------------------
'''Qn: check whether a person can vote or not based on the age'''

# age=int(input('Enter your age : '))
# if (age>=18):
#     print('you can vote')
#-----------------------------------------------------------------------------------
'''Qn--Ask the user for a value and check whether the given number is positive'''
# a=int(input('Enter a number : '))
# if a>0:
#     print(f'{a} is Positive')
# incase the user gives a negative value, the program displays nothing
#-----------------------------------------------------------------------------------
'''Qn---Ask the user for a value and check whether the given value is greater than 100'''
# a=int(input('Enter a number : '))
# if a>100:
#     print(f'{a} is greater than 100')
#------------------------------------------------------------------------------------
'''Qn---Ask the user for a value and check if the given value lies between 100 and 200.'''
#if yes---print number lies between 100 & 200
# a=int(input('Enter a number'))
# if a>100:
#     if a<200:
#         print(f'The given number {a} lies between 100 & 200')
#-----------------------------------------------------------------------------------
#Another way using AND

# a=int(input('Enter a number : ')) #a=101
# if a>100 and a<200: #101>100(T) and 101<200(T) ----> T
#     print(f'The given number {a} lies between 100 & 200')
#-----------------------------------------------------------------------------------
'''IF ELSE'''
#-----------------------------------------------------------------------------------
# if condition:
#     statement
# else:
#     statement
#-----------------------------------------------------------------------------------
'''Qn: check whether a person can vote or not based on the age'''

# age=int(input('Enter your age : '))
# if (age>=18):
#     print('you can vote')
# else:
#     print('you cant vote')
# Enter your age : 12
# you cant vote
#-----------------------------------------------------------------------------------
'''Qn--Ask the user for a value and check whether the given number is positive'''
# a=int(input('Enter a number : '))
# if a>0:
#     print(f'{a} is Positive')
# else:
#     print(f'{a} is Negative')

# Enter a number : -2
# -2 is negative
#-----------------------------------------------------------------------------------
'''Qn---Ask the user for a value and check whether the given value is greater than 100'''
# a=int(input('Enter a number : '))
# if a>100:
#     print(f'{a} is greater than 100')
# else:
#     print(f'{a} is less than 100')

# Enter a number : 15
# 15 is less than 100
# Enter a number : 150
# 150 is greater than 100
#-----------------------------------------------------------------------------------
'''Qn--Check if a given number is a multiple of 5 or not'''
# a=int(input('Enter a number : '))
# if a%5==0:
#     print(f'{a} is a multiple of 5')
# else:
#     print(f'{a} is not a multiple of 5')

# Enter a number : 12
# 12 is not a multiple of 5
# Enter a number : 50
# 50 is a multiple of 5
#-----------------------------------------------------------------------------------
'''Qn-- Check if a given number is a multiple of both 3 and 5'''
# a=int(input('Enter a number: '))
# if a%3==0 and a%5==0:
#     print(f'{a} is a multiple of 3 & 5')
# else:
#     print(f'{a} is not a multiple of 3 & 5')
# Enter a number: 56
# 56 is not a multiple of 3 & 5
#-----------------------------------------------------------------------------------
'''Write a program to check if a given number is even or odd'''

# a=int(input('Enter a number : '))
# if a%2==0:
#     print('The given number is even')
# else:
#     print('The given number is odd')

# Enter a number : 1
# The given number is odd
# Enter a number : 10
# The given number is even
#-----------------------------------------------------------------------------------
'''Qn: input a number from user and check if the last digit is a multiple of 3 '''
# a=int(input('Enter a number : '))
# c=a%10
# if c%3==0:
#     print(f'{c} in {a} is a multiple of 3')
# else:
#     print(f'{c} in {a} is not a multiple of 3')
# Enter a number : 103
# 3 in 103 is a multiple of 3
#-----------------------------------------------------------------------------------
'''Qn: input a number from user and check if the last two digit is a multiple of 3 '''
# a=int(input('Enter a number : '))
# c=a%100 ------------------#use 100 to extract the last two digits
# if c%3==0:
#     print(f'{c} in {a} is a multiple of 3')
# else:
#     print(f'{c} in {a} is not a multiple of 3')
'''this pgm doesnt work for numbers whose last digits are zero'''
# Enter a number : 100
# 0 in 100 is a multiple of 3
#-----------------------------------------------------------------------------------
# print(12%10) #o/p : 2
# print(123%100) #o/p 23
# print(1234%1000) #o/p 234
#-----------------------------------------------------------------------------------
