#1. comma separation
#2. f string format



#we are going to format strings
#1-comma separation
# num=10 #this number is 10 i want to display it like this in the output
#print('This number is ',num)

#we get an output like this number is 10
#----------------------------------------------------------
#if i want to add a full stop in the end

#print('this number is ',num,'.')
#-----------------------------------------------------------
#python will add a space when we use comma because the
#dot i used in the previous print statement inserted a space in the output
#--------------------------------------------------------
# create variables
# # fname = 'Ajmal'
# # lname = 'A'
# # age =30
# # color = 'red'
# Aim is to output: my name is ajmal A. my age is 26. my fav color is red

#print('my name is ',fname,lname,'.my age is',age,'.my fav color is',color)
#===================================================================================
#we discussed comma separation right now, if we dont use comma, it shows an error
#lets look at f string method
#======================================
#--'F' STRING METHOD
#num=10 #this number is 10
# print(f'this number is{num}') #if i change the space b/w is{num}, it reflects in the o/p. this is not in comma separation
# print(f'this number is {num}') # here i added an extra space and it is reflected in the o/p

#---------------------------------------------------------------------------------------------
#lets do the problem we solved using comma with this f string

# fname = 'Ajmal'
# lname = 'A'
# age =30
# color = 'red'
# print(f'my name is {fname} {lname}. my age is {age}. my fav color is {color}')

'''output:my name is ajmal A. my age is 26. my fav color is red'''
#--------------------------------------------------------------------------------------------