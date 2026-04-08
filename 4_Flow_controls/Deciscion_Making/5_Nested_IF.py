#nested if
'''Three categories are there'''

'''method 1'''
# if condition 1:
#     if condition2:
#         statement1
#     else:
#         statement2

'''method 2'''
# if condition1:
#     statement1
# else:
#     if condition2:
#         statement
#     else:
#         statement
'''method 3'''

# if condition1:
#     if condition:
#         statement
#     else:
#         statement
# else:
#     if condition:
#         statement
#     else:
#         statement
#------------------------------------------------------------
'''Qn:1--program to check a given number is +ve,-ve or zero'''

# n=int(input('Enter a number : '))
# if n!=0:
#     if n>0:
#         print('Positive')
#     else:
#         print('Negative')
# else:
#     print('Zero')
#-------------------------------------------------------------
'''using another method'''
# n=int(input('Enter a number : '))
# if n==0:
#     print('Zero')
# else:
#     if n>0:
#         print('Positive')
#     else:
#         print('Negative')
#-------------------------------------------------------------
'''1.Write a program to calculate the electricity bill . Accept the number of units from user  .

           unit                price 
  
    first 100 unit           No charge 

    next  100 unit           Rs 5 per unit 

    After 200 units          Rs 10 per unit 

# 350  == 100   100   150
           0  + 500 + 1500 ===2000 

# 250 ===100 100  50               
          0  500  500===1000   0 + 500 + (unit-200)10

# 150 === 100 50
           0  250        0+ (unit-100)5'''

# u=int(input('Enter the number of units : '))
# if u<=100:
#     print('Free')
# elif u>100 and u<=200:
#     print(f'Pay {(u-100)*5} rupees')
# elif u>200:
#     a=u-200
#     b=u-100-a
#     print(f'Pay {(b*5)+((a*10))} Rupees')
#---------------------------------------------------

'''2.Write a program that asks the user for their age and citizenship status (yes or no). If the user is 18 or older, check if they are a citizen.
  If both conditions are true, print "Eligible to vote", otherwise print "Not eligible".'''

# a=int(input('Enter your age : '))
# if a>=18:
#     b=input('Enter whether you are a citizen or not (yes/no): ')
#     if b=='yes':
#         print('You are Eligible to vote')
#     else:
#         print("Not eligible")
# else:
#     print('Not eligible')
#-------------------------------------------------------------
'''3.Ask the user for three angles. If the angles sum to 180, check further:

     If all angles are equal → "Equilateral triangle"

     If two angles are equal → "Isosceles triangle"

     Else → "Scalene triangle"

     If the sum isn’t 180, print "Not a triangle".'''


# a=int(input('Enter angle 1 : '))
# b=int(input('Enter angle 2 : '))
# c=int(input('Enter angle 3 : '))
# t=a+b+c
# if t==180:
#     if a==b==c:
#         print('Equilateral triangle')
#     elif a==b or b==c or a==c:
#         print('Isosceles triangle')
#     else:
#         print('Scalene triangle')
# else:
#     print('Not a triangle')
#-----------------------------------------------------------------
'''4. Input from the user. Checks whether the number is positive. If it is positive, further check whether it is even or odd.'''

# n=int(input('Enter a number : '))
# if n>0:
#     if n%2==0:
#         print('Even')
#     else:
#         print('Odd')
# else:
#     print('Enter a positive number')
#-----------------------------------------------------------------------
'''5.  find Largest Among three numbers using Nested if.'''

a=int(input('Enter num 1 : '))
b=int(input('Enter num 2 : '))
c=int(input('Enter num 3 : '))
if a==b or b==c or a==c:
    if a>c or a>b:
        print(f'{a} is larger')
    elif a<c:
        print(f'{c} is larger')
    else:
        print(f'{b} is larger')
else:
    if a>b and a>c:
        print(f'{a} is larger')
    elif b>a and b>c:
        print(f'{b} is larger')
    else:
        print(f'{c} is larger')





