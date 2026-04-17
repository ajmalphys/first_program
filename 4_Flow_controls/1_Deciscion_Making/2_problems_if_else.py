'''--Qn--BONUS PROBLEM
A company has decided to give a 5% bonus to employees who have more than 5 years of experience
write a python program to take the employees experience and salary as input. if the employee is eligible
calculate and print the bonus amount
if not, print that the employee is not eligible for a bonus'''

# n=int(input('Enter the years of Experience : '))
# if n>5:
#     s=int(input('Enter the salary : '))
#     bonus=(0.05*s)
#     print(f'The bonus is {bonus} Rupees' )
# else:
#     print('You are not eligible for a bonus')
#O/P=============================================
# Enter the years of Experience : 10
# Enter the salary : 1000
# The bonus is 50.0 Rupees
#-----------------------------------------------------------------------------------
''''--Qn.2_ PASSWORD CHECK
Ask the user to enter a password. if the password is equal to 'admin123',print
'Access granted' , otherwise print "Access denied" '''

# p=input('Enter the password : ')
# if p=='admin123':
#     print('Access granted')
# else:
#     print('Access denied')
# O/P================================
# Enter the password : admin123
# Access granted
# Enter the password : AJMAL
# Access denied
#-----------------------------------------------------------------------------------
'''--Qn.3--USERNAME AND PASSWORD CHECK
ask the user to enter the username and password. if the username is "admin" and
password is "1234", print "Login Successful", otherwise print "invalid credentials".'''

# u=input("Enter the username : ")
# p=input('Enter the password : ')
# if u=='admin' and p=='1234':
#     print('ACCESS GRANTED')
# else:
#     print('ACCESS DENIED')
#O/P================================
# Enter the username : admin
# Enter the password : 1234
# ACCESS GRANTED
# Enter the username : ADMIN
# Enter the password : 1234
# ACCESS DENIED
#-----------------------------------------------------------------------------------
'''---Qn--4.ATM Withdrawal---------------------
A user has a balance of 10,000. Ask for a withdrawal amount. If the amount is 
less than or equal to balance, print "Transaction Successful", otherwise print 
"Insufficient Balance".'''

# w=int(input('Enter the withdrawal amount : '))
# if w<=10000:
#     print('Transaction Successful')
# else:
#     print('Insufficient Balance')
#O/P====================================
# Enter the withdrawal amount : 10000
# Transaction Successful
# Enter the withdrawal amount : 2000000
# Insufficient Balance
#-----------------------------------------------------------------------------------
'''---Qn--5.Number Guessing (Basic)----------------------
Store a number (e.g., 7). Ask the user to guess. If correct, print "Correct Guess",
 otherwise print "Wrong Guess"'''

# n=int(input('Guess a number : '))
# if n==5:
#     print('Correct Guess')
# else:
#     print('Wrong Guess')
#O/P==========================
# Guess a number : 5
# Correct Guess
# Guess a number : 2
# Wrong Guess
#-----------------------------------------------------------------------------------
'''--Qn--6.Shopping Discount-------------------------
A customer purchased an item from a store. Write a Python program 
to take the purchase amount as input. If the amount is greater than 1000, calculate and 
display a 10% discount. Otherwise, display that no discount is applicable.'''

# p=int(input('Enter the purchase amount : '))
# if p>1000:
#     d=p*0.1
#     print(f'you got a discount of {d} Rupees')
# else:
#     print(f'Discount is not eligible for {p} Rupees')
#O/P===============================
# Enter the purchase amount : 2000
# you got a discount of 200.0 Rupees
# Enter the purchase amount : 500
# Discount is not eligible for 500 Rupees
#-----------------------------------------------------------------------------------