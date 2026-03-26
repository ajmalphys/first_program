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
#Qn: check whether a person can vote or not based on the age

# age=int(input('Enter your age : '))
# if (age>=18):
#     print('you can vote')
#-----------------------------------------------------------------------------------
#Qn--Ask the user for a value and check whether the given number is positive
# a=int(input('Enter a number : '))
# if a>0:
#     print(f'{a} is Positive')
# incase the user gives a negative value, the program displays nothing
#-----------------------------------------------------------------------------------
#Qn---Ask the user for a value and check whether the given value is greater than 100
# a=int(input('Enter a number : '))
# if a>100:
#     print(f'{a} is greater than 100')
#------------------------------------------------------------------------------------
#Qn---Ask the user for a value and check if the given value lies between 100 and 200.
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
