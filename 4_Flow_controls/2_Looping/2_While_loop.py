''''''
''' print Hello 5 times'''

# print('Hello') #1
# print('Hello') #2
# print('Hello') #3
# print('Hello') #4
# print('Hello') #5

'''this is not a proper way
Lets use while loop for this'''
#-----------------------------------------------------------
# i=1                     #initialisation
# while i<=5:             #condition
#     print(f'{i}.Hello')
#     i+=1                #increment
#O/P:----------------------------------
# 1.Hello
# 2.Hello
# 3.Hello
# 4.Hello
# 5.Hello
#--------------------------------------------------------------
'''Qn.1 : print 1 to 10 using while loop'''

# i=1
# while i<11:
#     print(i)
#     i+=1
#---------------------------------------------------------------
'''Qn.2 : print 20->35 using while loop'''
# i=20
# while i<=35:
#     print(i)
#     i+=1
#-----------------------------------------------------------------
'''Qn.3 : print from 25 to 1 using while loop'''

# i=25
# while i>0:
#     print(i)
#     i-=1
#-----------------------------------------------------------------
'''Qn.4 : Ask the user for the upper value and print from 1-> the upper value'''
#n=int(input('Enter the upper limit : '))
# i=1
# while i<=n:
#     print(i)
#     i+=1
#----------------------------------------------------------------------
'''Qn.5 : Ask the user for the lower and upper value, then print from lower to upper value'''
# l=int(input('Enter the lower value : '))
# u=int(input('Enter the upper value : '))
# if l<u:
#     i=u
#     while l<=u:
#         print(l)
#         l+=1
# else:
#     print('the lower upper order is reversed')
#----------------------------------------------------------------------------
'''Qn.6 :  print the even numbers in the range 1-20'''
# i=2
# while i<=20:
#     print(i)
#     i+=2
#----------------------------------------------------------------------------
# i=1
# while i<=20:
#     if i%2==0:
#         print(i)
#     i+=1
#----------------------------------------------------------------------------
'''Qn.7 : read the lower and upper value from the user and print the even numbers and odd numbers from lower to upper value'''
# l=int(input('Enter the lower value : '))
# u=int(input('Enter the upper value : '))
# if l<u:
#     while l<=u:
#         if l%2==0:
#             print(f'{l} is even')
#         else:
#             print(f'{l} is odd')
#         l+=1
# else:
#     print('Order is reversed')
#----------------------------------------------------------------------------
'''Qn.8 : create a multiplication table based on user input'''
# n=int(input("Enter the number : "))
# i=1
# while i<=10:
#     print(f'{i}x{n}={i*n}')
#     i+=1
#----------------------------------------------------------------------------
'''Qn.9 : find the sun of n natural numbers'''
# n=int(input('Enter n : '))
# i=1
# s=0
# while i<=n:
#     s+=i
#     i+=1
# print(f'Sum: {s}')
#----------------------------------------------------------------------------
'''Qn.10 : write a program to find the sum of even numbers below 100 '''
# i=1
# s=0
# while i<100:
#     if i%2==0:
#         s+=i
#     i+=1
# print('The sum of even numbers below 100 are :',s)
#O/P: The sum of even numbers below 100 are : 2450
#----------------------------------------------------------------------------
'''Qn.11 : program to find the sum of odd numbers below 100'''
# i=1
# s=0
# while i<100:
#     if i%2!=0:
#         s+=i
#     i+=1
# print('Sum of odd nos are: ',s)
#----------------------------------------------------------------------------
'''Qn.12 : program to find the sum of odd & even numbers below 100'''
# i=1
# so=0
# se=0
# while i<100:
#     if i%2==0:
#         se+=i
#     else:
#         so+=i
#     i+=1
# print(f'Odd sum : {so}')
# print(f'Even sum : {se}')
#o/p:
# Odd sum : 2500
# Even sum : 2450
#----------------------------------------------------------------------------
'''Qn.13 : program to find the factorial of a given number'''
# n=int(input('Enter the number: '))
# i=1
# f=1
# while i<=n:
#    f=f*i
#    i+=1
# print(f'Factorial : {f}')
#O/P
# Enter the number: 0
# Factorial : 1
#----------------------------------------------------------------------------
'''Qn.14 : program to collect digits from a given number '''
# n=int(input('Enter a number : '))
# while n>0:
#     print(n%10)
#     n=n//10 #floor division
#----------------------------------------------------------------------------
'''07.04.2026---Tuesday'''
#----------------------------------------------------------------------------
'''Qn.15 : program to find the sum of digits of a given number '''
# n=int(input('Enter a number : '))
# t=0
# while n>0:
#     t=t+(n%10)
#     n=n//10
# print(f'Total : {t}')
#----------------------------------------------------------------------------
'''Qn.16 : program to reverse a number using while loop '''
# n=int(input('Enter a number : '))
# x=0
# while n>0:
#     x=(n%10)+(10*x)
#     n=n//10
# print(f'reversed value is: {x}')
#----------------------------------------------------------------------------
'''end parameters : adds something to the end of something we wish to print'''
# print('Hello',end='123')
# print('Hello',end=',')
#----------------------------------------------------------------------------

# n=int(input('Enter a number : '))
# while n>0:
#     x=n%10
#     print(x,end='')
#     n=n//10
#----------------------------------------------------------------------------
'''Qn.17 : program for Armstrong Number (A numb that is equal to the sum of cubes of its digits) '''
'''153=(1^3)+(5^3)+(3^3)
1534=(1^4)+(5^4)+(3^4)+(4^4)'''
'''lets consider 3 digit case now'''

# n=int(input('Enter a three digit number : '))
# temp=n
# sum=0
# while n>0:
#     x=n%10
#     sum=sum+(x**3)
#     n//=10
# if (sum==temp):
#     print('its an armstrong number')
# else:
#     print('Not an armstrong number')
#----------------------------------------------------------------------------
'''there was a limitation. such that we can only use the previous program for 3 digit numbers only
so i modified it to accomodate any digit number'''
# n=int(input('Enter a number : '))
# temp1=n
# temp2=n
# temp3=n
# sum=0
# count=0
# while temp1>0:
#     count+=1
#     temp1//=10
# k=count
# print(count)
# while temp2>0:
#     x=temp2%10
#     sum=sum+(x**k)
#     temp2//=10
# if (sum==temp3):
#     print('its an armstrong number')
# else:
#     print('Not an armstrong number')


#----------------------------------------------------------------------------
'''Qn.18 : Harshad (Niven) number'''
'''A number that is divisible by the sum of its digits'''

# n=int(input('Enter a number : '))
# t1=n
# sum=0
# while n>0:
#     sum+=(n%10)
#     n//=10
# if t1%sum==0:
#     print('Its Harshad number')
# else:
#     print('Not Harshad')
#O/P
# Enter a number : 18
# Its Harshad number
#----------------------------------------------------------------------------
'''Qn.19 : Perfect number'''
''' A number whose sum of proper divisors (excluding itself) equals the number'''
''' example : 6--- 
Divisors : 1,2,3
1+2+3=6
so 6 is a perfect number
if not equal, print Not a perfect number'''

# n=int(input('Enter a number : '))
# sum=0
# t1=n
# i=1
# while i<=(n/2): #since factor of a number can max be equal to its half. a factor may not be larger beyond its half
#     if n%i==0:
#         sum+=i
#     i+=1
# if (sum==t1):
#     print('Perfect number')
# else:
#     print('Not perfect')
# #output:
# # Enter a number : 6
# # Perfect number
#----------------------------------------------------------------------------
'''Qn.20 : Strong Number
   A number whose sum of factorials of digits equals the number.
   Example: 145
   1! + 4! + 5! = 1 + 24 + 120 = 145
   So, 145 is a Strong number.
   If not equal, print Not a Strong number.'''

# n=int(input('Enter a number : '))
# t1=n
# sum=0
#
# while n>0:
#     p=n%10
#     fact=1
#     while p>0:
#         fact=fact*p
#         p-=1
#     sum=sum+fact
#     n//=10
# if (sum==t1):
#     print('Strong number')
# else:
#     print('Not a strong number')
# # o/p||||||||||||||||||||||||||||||||||||
# # Enter a number : 40585
# # Strong number

#----------------------------------------------------------------------------
'''Qn.21 : Automorphic Number
   A number whose square ends with the same number.
   Example: 25
   25² = 625 → ends with 25
   So, 25 is an Automorphic number.
   If not ending with same digits, print Not an Automorphic number.'''

# n=int(input('Enter a number : '))
# t1,t2=n,n #storing the input value to a temporary variable to compare at last
# sqr=n*n
# #if its 25, then need to check the last two digits of 625.
# #it its 250, then we need to check the last three digits and so on.
# #so we need to count the digits in the input number, then use that count for extracting the last digits of squared value.
# count=0
# while t1>0:
#     count+=1
#     t1//=10
# print(f'The given number has {count} digits')
# end_number=sqr%(10**count)
# if (end_number==t2):
#     print('Its an Automorphic number')
# else:
#     print('Not an Automorphic number')
# o/p:-----------------------------
# Enter a number : 76
# The given number has 2 digits
# Its an Automorphic number
# -------------------------------
# Enter a number : 6
# The given number has 1 digits
# Its an Automorphic number
# ---------------------------------
# Enter a number : 123
# The given number has 3 digits
# Not an Automorphic number
# ---------------------------------
# Enter a number : 625
# The given number has 3 digits
# Its an Automorphic number



#----------------------------------------------------------------------------
'''Qn.22 :  Neon Number
   A number where the sum of digits of its square equals the number itself.
   Example: 9
   9² = 81
   8 + 1 = 9
   So, 9 is a Neon number.
   If not equal, print Not a Neon number.'''

# n=int(input('Enter a number : '))
# sqr=n*n
# sum=0
# while sqr>0:
#     sum+=sqr%10
#     sqr//=10
# if (n==sum):
#     print('Yes, Neon Number')
# else:
#     print('Not a neon number')
# '''O/P:'''
# # Enter a number : 526454545
# # Not a neon number
# # ----------------------------------------
# # Enter a number : 9
# # Yes, Neon Number
# # ----------------------------------------
# # Enter a number : 0
# # Yes, Neon Number
# # ----------------------------------------
# # Enter a number : 1
# # Yes, Neon Number
#----------------------------------------------------------------------------
'''Qn.23 : Spy Number
   A number where the sum of digits equals the product of digits.
   Example: 1124
   Sum = 1 + 1 + 2 + 4 = 8
   Product = 1 × 1 × 2 × 4 = 8
   So, 1124 is a Spy number.
   If not equal, print Not a Spy number.'''

# n=int(input('Enter a number : '))
# sum=0
# pdt=1
# while n>0:
#     sum+=n%10
#     pdt*=n%10
#     n//=10
# if pdt==sum:
#     print('Its a spy number')
# else:
#     print('Not a spy number')
# o/p:-------------------------
# Enter a number : 1124
# Its a spy number
# ----------------------------------------
# Enter a number : 123
# Its a spy number
# ----------------------------------------
# Enter a number : 12
# Not a spy number
#----------------------------------------------------------------------------
'''Qn.24 : Disarium Number
   The sum of digits raised to the power of their position equals the number.
   Example: 135
   1¹ + 3² + 5³ = 1 + 9 + 125 = 135
   So, 135 is a Disarium number.
   If not equal, print Not a Disarium number.'''

# n=int(input('Enter a number : '))
# sum=0
# count=0
# t1,t2=n,n
# while t1>0:
#     count+=1
#     t1//=10
# print(f'there are {count} digits')
# while t2>0:
#     k=t2%10
#     sum+=(k**count)
#     count-=1
#     t2//=10
# if n==sum:
#     print('its a Disarium number')
# else:
#     print('Its not a Disarium number')
# o/p----------------------------------------
# Enter a number : 123
# there are 3 digits
# Its not a Disarium number
# -----------------------------------------
# Enter a number : 135
# there are 3 digits
# its a Disarium number

#----------------------------------------------------------------------------
'''Qn.25 : Duck Number
   A number that contains zero(s) but does not start with zero.
   Example:
   1203 → contains 0 (Valid)
   0123 → starts with 0 (Invalid)
   So, 1203 is a Duck number.
   If no zero or starts with 0, print Not a Duck number.'''

#need to detect whether there is zero or not
#need to detect the position of this zero

#----------------------------------------------------------------------------
# n=input('Enter a number: ') #inputing the number as string
# cd=len(n) #counts the digits in n
# #print(f'There are {cd} digits in the given number')
# av=int(n)
# #print(type(av))
# #print(av)
# zc=0
# if av//(10**(cd-1))==0: #this floor division is performed to eliminate the terms till the first digit
#     print('Not a duck number. Reason: First digit is zero')
# else:
#     while av>0:
#         #print('Checking number of zeroes')
#         if av%10==0:
#             zc+=1 #zero counter
#         av//=10     #120
#     #print('Zero counter : ',zc)
#     if zc!=0:
#         print(f'its a Duck number with {zc} zeroes')
#     else:
#         print('Not a duck number. Reason: No zeroes are there')
# #output
# #Enter a number: 1203
# #its a Duck number with 1 zeroes
# # Enter a number: 0123
# # Not a duck number. Reason: First digit is zero


#----------------------------------------------------------------------------