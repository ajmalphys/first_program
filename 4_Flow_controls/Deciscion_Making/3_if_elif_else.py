#Syntax
# if condition1:
#     statement 1
# elif condition 2:
#     statement 2
# elif condition 3:
#     statement 3
# else:
#     statement 4
#------------------------------------------------------------------------
'''Qn.1 : wite a pgm to find a given number is positive , negative or zero'''

# n=int(input('Enter a number : '))
# if n>0:
#     print('Positive')
# elif n<0:
#     print('Negative')
# else:
#     print('Given number is zero')
#o/p-------------------------------------
# Enter a number : 5
# Positive
# Enter a number : -9
# Negative
# Enter a number : 0
# Given number is zero
#--------------------------------------------------------------------------------------------
'''Qn:2--write a program to find the largest among two numbers'''

# a=int(input('Enter the First number :'))
# b=int(input('Enter the Second number :'))
# if a>b:
#     print(f'{a} is largest')
# elif b>a:
#     print(f'{b} is largest')
# else:
#     print('both numbers are equal')
#o/p---------------------------------------
# Enter the First number :1
# Enter the Second number :10
# 10 is largest
# Enter the First number :20
# Enter the Second number :5
# 20 is largest
# Enter the First number :15
# Enter the Second number :15
# both numbers are equal

#------------------------------------------------------------------------------------------
'''Qn:3--write a prgram to find the largest among given three numbers'''
a=int(input('Enter num1 : '))
b=int(input('Enter num2 : '))
c=int(input('Enter num3 : '))
if a==b and a>c:                #24-24-12
    print(f'{a} is larger')
elif a==c and a>b:              #24_12_24
    print(f'{a} is larger')
elif b==c and b>a:              #12_24_24
    print(f'{b} is larger')
elif a>b and a>c:
    print(f'{a} is larger')
elif b>a and b>c:
    print(f'{b} is larger')
elif c>a and c>b:
    print(f'{c} is larger')
else:
    print('Given numbers are equal')
#O/P-----------------------------
# Enter num1 : 1
# Enter num2 : 2
# Enter num3 : 1
# 2 is larger
#------------------------
# Enter num1 : 1
# Enter num2 : 1
# Enter num3 : 2
# 2 is larger
#--------------------------
# Enter num1 : 2
# Enter num2 : 2
# Enter num3 : 1
# Given numbers are equal
#---------------------------
# Enter num1 : 2
# Enter num2 : 1
# Enter num3 : 2
# Given numbers are equal
#----------------------------
# Enter num1 : 1
# Enter num2 : 2
# Enter num3 : 3
# 3 is larger
#--------------
# Enter num1 : 3
# Enter num2 : 2
# Enter num3 : 1
# 3 is larger
#---------------
# Enter num1 : 1
# Enter num2 : 3
# Enter num3 : 2
# 3 is larger
#------------------
# Enter num1 : 0
# Enter num2 : 0
# Enter num3 : 0
# Given numbers are equal
#----------------------------
# Enter num1 : 24
# Enter num2 : 24
# Enter num3 : 12
# Given numbers are equal
#-----------------------------
#o/p after correction
# Enter num1 : 2
# Enter num2 : 2
# Enter num3 : 1
# 2 is larger
#-----------------------------------------------------------------------------------
'''Qn:4-- write a program to check if the given year is leap year or not'''

# y=int(input('Enter an year : '))
# if y%4==0 and y%100!=0 or y%400==0:
#     print('Its a leap year')
# else:
#     print('Not a leap year')
#o/p:.............................
# Enter an year : 2000
# Its a leap year
# Enter an year : 1500 its a century year, divisible by 4, but not with 400. so not a leap year
# Not a leap year