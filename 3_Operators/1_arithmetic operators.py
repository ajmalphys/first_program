# num1=10
# num2=11
# print(num1+num2)
'''------------------------------------------------------------'''
#Qn----ask the user for three numbers and perform its addition

#o/p format first num + second num + third num = answer
# a=int(input('enter the first number: '))
# b=int(input('enter the second number: '))
# c=int(input('enter the third number: '))
# print(f'{a} + {b} + {c} = {a+b+c}') #using f string here to format the desired output
'''------------------------------------------------------------'''
#obtained output
# enter the first number: 1
# enter the second number: 1
# enter the third number: 1
# 1 + 1 + 1 = 3
''''------------------------------------------------------------'''
#CONCATENATION

# name=('python')
# age='2'
# print(name+age)
#o/p
#python2
'''-----------------------------------------------------------------'''
#qn: ask the user for two values and perform
#1.Substraction
#2.Multiplication
#3.Division

# a=int(input('enter the first number: '))
# b=int(input('enter the second  number: '))
# print(f'The difference is : {a-b}')
# print(f'The Product is : {a*b}')
# print(f'The quotient is : {a/b}')
# print(f'the remainder is : {a%b}')

#output
# enter the first number: 10
# enter the second  number: 5
# The difference is : 5
# The Product is : 50
# The quotient is : 2.0
'''---------------------------------------------------------------------------'''
'''modulus operator % ------ used to fetch the remainder---- the left over of a division'''
# a=int(input('enter the first number : '))
# b=int(input('enter the second number : '))
# print(f'The remainder of {a} & {b} is {a%b}')
#-----------------------------------------------------
# print(9%2)
# print(11%2)
# print(8%2)
# print(12%5)
#op
# 1
# 1
# 0
# 2
#--------------------------------------------------------

'''floor division---- used to remove the decimal part(//)'''

#9/2=4.5----->9//2=4 the floor division removes the decimal part
# print(9/2,',',9//2)
# print(11/3,',',11//3)
#output
#4.5 , 4
#3.6666666666666665 , 3
#----------------------------------------------------
'''Ask the user for two numbers and perform floor division'''

# a=int(input('Enter the first number : '))
# b=int(input('Enter the Second number : '))
# print(f'The floor division result is {a//b}')
#output
#Enter the first number : 3
# Enter the Second number : 2
# The floor division result is 1
#---------------------------------------------------------
'''EXPONENTIAL OPERATOR'''

#2**2 ----->2^2
#2**3 ----->2^3

a=int(input('Enter the base : '))
b=int(input('Enter the exponent : '))
print(f'The result is {a**b}')
#---------------------------------------------------------
