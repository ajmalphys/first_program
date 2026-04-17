''''''
'''FOR LOOP'''
'''WHILE LOOP  was based on a condition
it is different from while loop
syntax of FOR loop:
for iterable in range(start, stop, step): 
In a while loop, the execution is condition-dependent: "Keep doing this as long as this statement remains true."

In a for loop, the execution is collection-dependent: "Do this for every item that exists in this sequence."

The "Infinite" Factor##################################################################################################

One of the biggest differences is safety. Because a for loop in Python usually iterates over a 
fixed sequence (like range(10)), it is much harder to accidentally create an infinite loop. 
A while loop, however, will run forever if you forget to update the variable that satisfies the condition!
#######################################################################################################################
'''

'''Qn.1: print 'Hello' 5 times'''
# for i in range(0,5): #the loop will execute till the "stop-1" value. ---0,1,2,3,4 only and not 5
#     print('Hello')
'''
printing is done based on range and not checking any condition
in while loop printing was done until a condition is met
but in for loop, iteration is done based on the given range and dont rely on any condition
the range works in FOR loop as (start value, stopvalue-1)

working:-------------------------------------------------========---------==========----------==========-------=======
i is the iterating variable
the first value in range is 0
at first loop, i is assigned to a value=0
now i=0
and it prints hello
then it increments the value by i=1
and again prints hello
thus, the value of i increases till i=4
it will stop there since its just below the higher stop limit 5

Using the range() Function--------------------------------------------------------------------------------------------------------------

If you need to run a block of code a specific number of times, use the range() function.

    range(5): 0, 1, 2, 3, 4

    range(2, 6): 2, 3, 4, 5

    range(0, 10, 2): 0, 2, 4, 6, 8 (Starts at 0, ends before 10, increments by 2)
    
The else Clause-------------------------------------------------------------------------------------------------------------------------------

Unique to Python, you can use an else block after a for loop. The code in else runs only if the loop finishes normally 
(i.e., it was not interrupted by a break).

for i in range(3):
    print(i)
else:
    print("Loop finished successfully!")
'''
#--------------------------------------------------------------------------------------------------
'''Qn.2 : print from 1 to 25 using for loop'''
# for i in range (1,26):
#     print(i)
#--------------------------------------------------------------------------------------------------
'''Qn.3 : print from 1 to 25 using for loop straight'''
# for i in range (1,26)
#     print(i,end=',')
#--------------------------------------------------------------------------------------------------
'''Qn.4: print from 25 to 40 using for loop'''
# for i in range(25,41):
#     print(i,end=',')
# --------------------------------------------------------------------------------------------------
'''Qn.5: print from 25 to 1 using for loop'''
# for i in range (25,0,-1):
#     print(i,end=',')
# --------------------------------------------------------------------------------------------------
# for i in range(9): #a single value act as a stop value, start value will be considered as 0 and step as 1
#     print(i,end=',')
# --------------------------------------------------------------------------------------------------
'''Qn.6: ask the user for upper value and print from 1 to the upper value'''
# n=int(input('Enter the upper limit : '))
# for i in range (1,n+1):
#     print(i, end=',')
# --------------------------------------------------------------------------------------------------
'''Qn.7: write a program to find the even numbers in the range 1 to 20'''
# for i in range(1,21):
#     if i%2==0:
#         print(i,end=' ')
#o/p:2 4 6 8 10 12 14 16 18 20
# --------------------------------------------------------------------------------------------------
'''Qn.8:WAP for even numbers b/w the given range from the user '''
# l=int(input('Enter the lower limit : '))
# u=int(input('Enter the upper limit : '))
# for i in range (l,u+1):
#     if i%2==0:
#         print(i,end=' ')
#output-------
# Enter the lower limit : 3
# Enter the upper limit : 23
# 4 6 8 10 12 14 16 18 20 22
#--------------------------------------------------------------------------------------------------
'''Qn.8:WAP to find the sum of n natural numbers using for loop '''
# n=int(input('Enter the number : '))
# sum=0
# for i in range (n+1):
#     sum+=i
# print('Sum =',sum)
#--------------------------------------------------------------------------------------------------
'''Qn.9:find the sum of odd nos and even nos below 100 respectively'''
# so=0 #sum of odd nos
# se=0 #sum of even nos
# l=int(input('Enter lower limit : '))
# u=int(input('Enter upper limit : '))
# if u<100:
#     for i in range(l,u+1):
#         if i%2==0:
#             se+=i
#         else:
#             so+=i
#     print(f' Sum of Odd : {so} & Even : {se}')
# else:
#     print('enter an upper limit below 100')
#--------------------------------------------------------------------------------------------------
'''Qn.10: print nos from 1 to 50 divisible by 5'''
# for i in range(1,51):
#     if i%5==0:
#         print(i,end=' ')
#output:5 10 15 20 25 30 35 40 45 50
#--------------------------------------------------------------------------------------------------
'''Qn.11: find the factorial of a given number'''
# n=int(input('Enter a number : '))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(f'{n}! = {fact}')
#--------------------------------------------------------------------------------------------------
'''Qn.12: check if a given number is perfect number using for loop''' #number = sum of its divisors

# n=int(input('Enter a number : '))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print(f'{n} is a perfect number')
# else:
#     print(f'{n} is not a perfect number')
#output
# Enter a number : 496
# 496 is a perfect number--------
# Enter a number : 490
# 490 is not a perfect number-------------
# Enter a number : 28
# 28 is a perfect number
#--------------------------------------------------------------------------------------------------
'''Qn.13: Sum of digits'''
# n=input('Enter a number : ')
# sum=0
# l=len(n)
# p=int(n)
# for i in range(l):
#     sum+=p%10
#     p//=10
# print(f'Sum of digits : {sum}')
#--------------------------------------------------------------------------------------------------
'''Qn.14:Reverse a Number (using for)
Input: 1234
Output: 4321'''
# n=input('Enter a number : ')
# rev='' #empty string--it is equivalent to assigning a zero while dealing with int
# for i in n:
#     rev=i+rev
# print(rev)
#output-----------------
# Enter a number : 123
# 321
#--------------------------------------------------------------------------------------------------
'''Qn.15: Palindrome Number
Check if number is same when reversed
'''

# n=input('Enter a number : ')
# rev=''
# for i in n:
#     rev=i+rev
# if(n==rev):
#     print('Palindrome')
# else:
#     print('Not palindrome')
#outpu---------------
# Enter a number : 121
# Palindrome
# Enter a number : 123
# Not palindrome
#--------------------------------------------------------------------------------------------------
'''Qn.16: Armstrong Number Check
Example: 153
(1³ + 5³ + 3³ = 153)
'''

# n=input('Enter a number : ')
# sum=0
# count=0
# for i in n:
#     count+=1
# for i in n:
#     sum+=int(i)**count
# if(int(n)==sum):
#     print('Armstrong number')
# else:
#     print('Not an armstrong number')
#output-----------------
# Enter a number : 153
# Armstrong number
# Enter a number : 255
# Not an armstrong number
# Enter a number : 1634
# Armstrong number
#--------------------------------------------------------------------------------------------------

'''Qn.17: Prime Number Check
Input: number
Output: Prime / Not Prime'''

# n=int(input('Enter a number: '))
# c=0 #a counting variable to show calculate the number of factors other than 1 and the same number itself
# for i in range(2,n): #range is set from 2 to n so that the LL=2 & UL=n-1. this excludes the common divisors of prime nos(1 & same no:)
#     if n%i==0:
#         c+=1
# if c==0:
#     print('Prime number')
# else:
#     print('Not a prime number')

#output-----------
# Enter a number: 7
# Prime number
# Enter a number: 125
# Not a prime number
#--------------------------------------------------------------------------------------------------
'''Qn.18: Print Numbers Divisible by 7 (1–100)
Print only multiples of 7'''

# for i in range(1,100): #since 98 is the number below 100 which is divisible by 7. it doesnt matter to use 100 or 101
#     if i%7==0:
#         print(i,end=' ')
#output-------------
#7 14 21 28 35 42 49 56 63 70 77 84 91 98
#--------------------------------------------------------------------------------------------------
'''Qn.19:Sum of Squares of Digits
Input: 123 → Output: 1² + 2² + 3² = 14
'''
# n=input('Enter a number : ') #inputing the number as string
# sum=0
# for i in n:
#     sum+=int(i)**2
# print(f'Sum of squares of digits : {sum}')
#output-----------------
# Enter a number : 123
# Sum of squares of digits : 14
#--------------------------------------------------------------------------------------------------
'''Qn.20: Check Perfect Number
A number whose sum of proper divisors (excluding itself) equals the number
Example: 6 → 1+2+3 = 6'''

# n=int(input('Enter a number : '))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print('Perfect number')
# else:
#     print('Not a perfect number')
#output
# Enter a number : 6
# Perfect number
# Enter a number : 28
# Perfect number
# Enter a number : 496
# Perfect number
# Enter a number : 29
# Not a perfect number
#--------------------------------------------------------------------------------------------------

