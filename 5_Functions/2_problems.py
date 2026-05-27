''''''
'''
Qn:1- wap to find the multiplication of two numbers using function(using 3 methods)'''

'''Method:1'''
# def mult():
#     a=int(input('Enter the first number : '))
#     b=int(input('Enter the second number : '))
#     print(f'{a}x{b}={a*b}')
'''------------calling the function------------------'''
# mult()
'''output
Enter the first number : 5
Enter the second number : 5
5x5=25
======================================================'''
'''Method:2'''
# def mult(a,b):
#     print(f'{a}x{b}={a*b}')
'''-------------calling the function-------------------'''
# mult(5,5)
'''output
5x5=25
======================================================'''
'''Method:3'''
# def mult(a,b):
#     c=a*b
#     return c
'''--------------calling the function------------------'''
# print(mult(5,5))
'''output
25
======================================================='''

'''
Qn:2 wap to find the factorial of a number using 3 methods'''

'''Method:1'''
# def fact():
#     n=int(input('Enter a number : '))
#     fact=1
#     while n>0:
#         fact=fact*n
#         n-=1
#     print(fact)
# fact()
'''output
Enter a number : 5
120'''

'''Method:2: package_example with argument and no return type'''
# def fact(n):
#     fact=1
#     while n>0:
#         fact=fact*n
#         n-=1
#     print(fact)
# fact(5)

'''Method:3: package_example with argument and return type'''
# def fact(n):
#     fact=1
#     while n>0:
#         fact=fact*n
#         n-=1
#     return fact
#
# print(fact(5))

'''Qn:3-wap to find the square of a number using functions'''

'''method 1'''

# def square():
#     n=int(input('Enter a number: '))
#     s=n*n
#     print(f'Square is : {s}')
# square()

'''method 2'''
# def square(n):
#     s=n*n
#     print(f'Square is : {s}')
# square(5)

'''method 3'''

# def square(n):
#     s=n*n
#     return s
# print(f'Square is : {square(5)}')

'''Qn:4- check if the given number is even or odd'''

'''method 2'''
# def identify(n):
#     if n%2==0:
#         print('Even')
#     else:
#         print('Odd')
# identify(5)
# identify(4)

'''method 3'''
# def identify(n):
#     if n%2==0:
#         return 'even'
#     else:
#         return 'odd'
#
# print(identify(4))
# print(identify(9))
'''-------------------------------------------------------------------------------'''

