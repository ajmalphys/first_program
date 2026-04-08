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



