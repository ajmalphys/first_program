#we are discussing input functions in this directory
'''--------------------------------------------------------------'''
'''input() is used to read a value from the user'''
'''--------------------------------------------------------------'''
# Program 1----------------------
# input('Enter your name : ')
# input('Enter your age : ')
# input('Enter your Password : ')
'''this will ask for data from the user'''
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
'''we need to store this input data into a variable'''
#--------------------------------------------------
# Program 2
# name=input('Enter your name : ') #this just asks only the inout from user
# print(name) #displays the value enterd by user
# print(f'the name entered is : {name}') #formatted output
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
'''>>>>>>>>>>>>>>>INPUT function reads all data as STRINGS<<<<<<<<<<<<<<<<<<<<<<'''
# Program 3
# age=input('Enter your age: ')
# print(age)
# print(type(age)) #output : <class 'str'>
#-----------------------------------------------------------------
'''how to convert this into an integer?'''
#Program 4
# age=int(input("Enter your age: ")) # this converts the input into int
# print(age)
# print(type(age)) #output : <class 'int'>
#-------------------------------------------
# Program 5
'''Qn : ask the user for their username and password, Display "your user name is _________ and user pswd is_______'''
username = input('enter the username : ')
password=input("Enter the password : ")
print(f'Your username is : {username} and your password is : {password}')
#output is : Your username is : ajmal and your password is : 123
#-----------------------------------------------------------------------------
