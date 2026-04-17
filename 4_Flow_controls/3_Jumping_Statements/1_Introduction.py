''''''
'''
break
continue
pass

---------Break-----------
it is used to exit from a loop
for i in range(1,10): it executes from i=1 to 10
    if i==5:
        break
    print(i)



'''

# for i in range(1,10): #it executes from i=1 to 10
#     if i==5:
#         break
#     print(i)

'''
---------COntinue----------
it skips a step
'''

# for i in range(1,10):
#     if i==5:
#         continue
#     print(i,end=' ')

'''Qn.1: print even nos using continue statement'''
# for i in range(1,101):
#     if i%2!=0:
#         continue
#     print(i, end=' ')

'''
-----------Pass--------
it does nothing'''
'''the following code generates a syntax error'''
# for i in range(1,6):
#     if i==2:
#     print(i)
#----------------------------------------------------------
'''this syntax error can be byepassed using pass'''
# for i in range(1,6):
#     if i==2:
#         pass
#     print(i,end=' ')
#output
# 1 2 3 4 5
#----------------------------------------------------------
# while True: #starting an infinite loop
#     print(1)
#----------------------------------------------------------
'''Qn.2: ask the user to enter a series of nos. stop accepting the input 
as soon as the user enter a negative number'''
# while True:
#     n=int(input('Enter a number : '))
#     if n<0:
#         print('Entered negative number, exiting...')
#         break
#----------------------------------------------------------
'''Qn.3: print all the numbers from 1 to 10 except for 5'''
# for i in range(1,11):
#     if i==5:
#         continue
#     print(i,end=' ')
#----------------------------------------------------------
''''Qn.4: print the square of numbers from 1 to 25, but skip any number that is divisible by 5'''
# for i in range(1,26):
#     if i**2%5==0:
#         print(f'Skipping {i**2}')
#         continue
#     print(i**2)
#----------------------------------------------------------
'''Qn.5:  Write a loop that iterates from0 to 4, if the number is 2 use pass. Otherwise print the number'''

# for i in range(0,5):
#     if i==2:
#         pass
#     print(i,end=' ')
#--------------------------------------------------------
'''Qn.6: Write a program that iterates through numbers from 1 to 20 . If a number is divisible by 3, 
skip that number.'''

# for i in range(1,21):
#     if i%3==0:
#         continue
#     print(i,end=' ')
#--------------------------------------------------------
'''Qn.7: If a number is greater than 15, exit the loop immediately. Use a pass statement in an else block within the 
loop for numbers that don't meet the condition.
Print all eligible numbers
'''
# while True:
#     n=int(input('Enter a number : '))
#     if n>15:
#         print('Exiting the loop')
#         break
#     else:
#         pass
#--------------------------------------------------------
'''Qn.8: Write a program to find the first number divisible by both 7 and 9 between 1 and 500, and stop after finding it.'''

# for i in range (1,501):
#     if i%7==0 and i%9==0:
#         print(f'{i} is the first number divisible by both 7 & 9')
#         break
#--------------------------------------------------------
'''Qn.9: =>--Shopping Cart Billing

Accept item prices continuously.

Skip items with price 0 or negative.

Stop when total bill exceeds 5000.'''
# sum=0
# while sum<5000:
#     n=int(input('Enter the price : '))
#     if n==0 or n<0:
#         continue
#     else:
#         sum+=n
# print('Total bill exceeded 5000')
#----------------------------------------------------
'''Qn.10: =>--Elevator Floor Control

Accept floor numbers:

Skip invalid floor numbers (<0 or >20)

Stop when floor 13 is entered (maintenance floor)'''
# while True:
#     f=int(input('Enter the floor number : '))
#     if f<0 or f>20:
#         print('Invalid floor')
#         continue
#     elif f==13:
#         print('Maintenance floor')
#         break
#--------------------------------------------------------
'''Qn.11: =>--Speed Monitoring System

Accept vehicle speeds:

Skip speeds < 10 km/h

Stop when speed exceeds 120 km/h'''
# while True:
#     s=int(input('Enter the speed : '))
#     if s<10:
#         continue
#     elif s>120:
#         print('Speed exceeded')
#         break
#--------------------------------------------------------
'''Qn.12: =>--Power Consumption Monitor

Accept daily power units:

Skip values < 1 unit

Stop when total consumption exceeds 300 units'''
# sum=0
# while True:
#     u=int(input('Enter the units : '))
#     if u<1:
#         continue
#     else:
#         sum+=u
#         if sum>300:
#             print(f'Total units {sum}/300 exceeded')
#             break
#--------------------------------------------------------
'''
1. Display a menu like this:

   **** MENU ***
   1. Addition
   2. Subtraction
   3. Multiplication
   4. Division
   5. Exit
   ```

2. Ask the user to enter their choice (1 to 4).

3. If the choice is 1 to 4:

    Ask the user to enter two numbers.
    Perform the selected operation and print the result.

4. If the user enters an invalid choice:

    Print "Wrong choice! Please enter a number between 1 and 5.


 Example Output:
**** MENU ****
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Enter choice: 3
Enter first number: 5
Enter second number: 4
Multiplication = 20'''
# Add a  while loop like while True to repeat the options again
# while True:
#     print('1.Addition')
#     print('2.Subtraction')
#     print('3.Multiplication')
#     print('4.Division')
#     print('5.Exit')
#     n=int(input('Enter your choice : '))
#     if n>5:
#         print('Invalid choice')
#     elif n<=4:
#         a=int(input('Enter the first number : '))
#         b=int(input('Enter the second number'))
#         if n==1:
#             print(f'{a} + {b} = {a+b}')
#         elif n==2:
#             print(f'{a} - {b} = {a-b}')
#         elif n==3:
#             print(f'{a} x {b} = {a*b}')
#         else:
#             print(f'{a} / {b} = {a/b}')
#     else:
#         if n==5:
#             break
#-----------------------------------------------------------------------------

