#three types of logical operators are there
#1.AND
#2.OR
#3.NOT

#  why we are using it : used to combine two or more operators

# a=10,20,30 # its a tuple, collection types, its a sequential data type
# print(a)
# print(type(a))
#------------------------------
# a,b=10,5
# print(a,b)
#o/p : 10 5
#-------------------
# a,b,c=1,2
# print(a,b,c)
# #o/p : error
#---------------------------------------------------------
'''AND : returns True only if both statements are True'''
from doctest import run_docstring_examples

#---------------------------------------------------------
# print(True and True)
# #o/p : True
#----------------------
# print(True and False)
#o/p : False
#=========================
'''Testing AND operation'''
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# a,b,c=10,10,5
# print(a>c and b>c) #10>5 (T) and 10>5 (T)
# #o/p : True
# #-----------------------------
# print(a>c and b<c) #10>5 (T) and 10<5 (F)
# #o/p : False
# #------------------------------
# print(a<c and b>c) #10<5 (F) and 10>5 (T)
# #o/p : Fasle
# #--------------------------------
# print(a<c and b<c) #10<5(F) and 10<5 (F)
# #o/p : False
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
'''OR Operator: returns true if any one of the statement is true'''
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# input         output
# True   True   True
# True   False  True
# False  True   True
# False  False  False
#----------------------------
# a,b,c=10,10,5
# print(a>c or b<c) #10>5(T) or 10<5(F)
# #o/p : True
# print(a<c or b>c) #10<5(F) or 10>5(T)
# #o/p : True
# print(a>c or b>c) #10>5(T) or 10>5(T)
# #o/p : True
# print(a<c or b<c) #10<5(F) or 10<5(F)
#o/p : False
#--------------------------------
'''logical NOT operator : used for negation purpose'''
#----------------------------------
# a,b=5,10
# print(a>b) #5>10 (F)
# #o/p : False
# print(not (a>b)) # negates the result False from a>b. the actual result is False. this 'NOT' turns it into 'True'
#----------------------------------------
'''MEMBERSHIP operator : checks if something is a member of something. the o/p would be True/False'''
'''Two MEMBERSHIP operators are there: IN and NOTIN'''
#-----------------------------------------
# s='python'
# print('t' in s) #checks whether 't' is there in 'python' or not #o/p : Truw
# print('t' not in s) #o/p : False #checks the statement 't' is not in 's'. thats false here bcoz 't' is there in 's'
# print('z' not in s) #o/p : True
#--------------------------------
''''ASSIGNMENT / COMPOUND ASSIGNMENT operator'''
'''its a shortcut to do the mathematical operations'''
#--------------------------------------------------------
# num=10 # i need to change it to 11 without changing its actual value
# num=num+1 #this is a way to do it. but its not the compound assignment

#-------------------------------------------------
#now we are going to use COMPOUND assignment
#--------------------------------------------------
# num=10
# num+=1
# print(num)
#-----------------------------------------------------
# num=20 # i want to change it to 15
# num-=5
# print(num)
#-----------------------------------------------------
# num=10 # change it to 20
# num+=10
# print(num)
#-----------------------------------------------------
# num=10
# num*=2 # we can use this compound assignment with every operators
# print(num)
#------------------------------------------------------
# +=
# -=
# *=
# /=
# %=
# **=
#-----------------------------------------------
# a=20
# b=30
# add=a+b
# add+=20
# print(add)
#-----------------------------------------------
'''swapping of two numbers'''
# a=10
# b=20
# print(f'Before swapping a={a} and b={b}')
# c=a
# a=b
# b=c
# print(f'After swapping a={a} and b={b}')
#----------------------------------------
# a=10
# b=20
# print(f'Before swapping a={a} and b={b}')
# a=a+b #a+=b
# b=a-b #b-=a we cannot do it in compound assignment
# a=a-b #a-=b
# print(print(f'After swapping a={a} and b={b}'))
#--------------------------------------------------
#Ask the user for two values and swap the numbers
a=int(input('Enter the 1 st number : '))
b=int(input('Enter the 2 nd number : '))
print(f'Before Swapping, 1 st number = {a} and 2 nd number ={b}')
c=a
a=b
b=c
print(f'After Swapping, 1 st number = {a} and 2 nd number ={b}')

