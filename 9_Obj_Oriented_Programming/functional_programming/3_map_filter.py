''''''
'''map



'''
'''map'''

# l=[1,2,3,4,5]
# l1=[]
# for i in l:
#     l1.append(i**2)
# print(l1) #[1, 4, 9, 16, 25]
#---------------------------------------------------------
# numbers = [1, 2, 3, 4, 5]
#
# # map() returns an iterator, so we wrap it in list() to see the results
# squared = list(map(lambda x: x**2, numbers))
#
# print(squared)  # Output: [1, 4, 9, 16, 25]

#----------------------------------------------------------------
'''filter'''
# l=[1,2,3,4,5,6,7,8,9]
# l1=[]
# for i in l:
#     if i%2==0:
#         l1.append(i)
# print(l1)  #[2, 4, 6, 8]
#-----------------------------------------------------------------------------
# syntax of map
# var_name=list(map(function,iterable))
#---------------------------------------------------------------------------
#syntax of filter
#var_name=list(filter(function,iterable)
#---------------------------------------------------------------------------
'''create a map to print the squares of the elemets in the given list'''
#----------------------------------------------
# syntax of map
# var_name=list(map(function,iterable))
#-----------------------------------------------
'''using normal function definition'''
# l=[1,2,3,4,5]
# def sq(num):
#     return num**2
# print(list(map(sq,l))) #[1, 4, 9, 16, 25]
#-------------------------------------------------------
'''using lambda expression'''
# l=[1,2,3,4,5]
# print(list(map(lambda a:a**2,l))) #[1, 4, 9, 16, 25]
#-------------------------------------------------------
'''find the cube of the numbers in a list'''
# l=[1,2,3,4,5]
# def cube(n):
#     return(n**3)
# print(list(map(cube,l))) #[1, 8, 27, 64, 125]
#---------------------------------------------------------
# l=[1,2,3,4,5]
# print(list(map(lambda a:a**3,l))) #[1, 8, 27, 64, 125]
#-----------------------------------------------------------
'''filter'''
'''collect even numbers using filter'''
# l=[1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda a:a%2==0,l))) #[2, 4, 6, 8, 10]
#------------------------------------------------------------
'''create a list & find the cube of odd nos from the lsit'''
# l=[1,2,3,4,5,6,7,8,9,10]
# o=list(filter(lambda a:a%2!=0,l)) #[1, 3, 5, 7, 9]
# print(o)
# print(list(map(lambda h:h**3,o))) # [1, 27, 125, 343, 729]
#------------------------------------------------------------
'''convert all the words in the list ['cat','dog','tiger'] to upper case using map and lambda'''

# l=['cat','dog','tiger']
# print(list(map(lambda a:a.upper(),l))) #['CAT', 'DOG', 'TIGER']
#------------------------------------------------------------------
'''add 5 to every number in the given list'''
# l=[10,20,30,40]
# print(list(map(lambda x:x+5, l))) #[15, 25, 35, 45]
#------------------------------------------------------------------
'''find the length of each word in the given list'''
# l=['apple','kiwi','banana']
# print(list(map(lambda x:len(x),l))) #[5, 4, 6]
#-------------------------------------------------------------------
'''From the list `[5, 10, 15, 20, 25]`, keep only the numbers greater than **12** using `filter` and a lambda'''

# l=[5, 10, 15, 20, 25]
# print(list(filter(lambda x:x>12,l))) #[15, 20, 25]
#-----------------------------------------------------------------------------------------
'''From `[3, 6, 9, 12, 15]`, filter only the numbers divisible by **6** using `filter` and a lambda.'''

# l=[3, 6, 9, 12, 15]
# print(list(filter(lambda x:x%6==0,l))) #[6, 12]
#-----------------------------------------------------------------
'''From `[11, 22, 33, 44, 55]`, filter out all *odd* numbers using `filter` and a lambda.'''

# l=[11, 22, 33, 44, 55]
# print(list(filter(lambda x:x%2!=0,l))) #[11, 33, 55]
#------------------------------------------------------------------------
'''From `["apple", "an", "cat", "ok"]`, filter only the words with length *greater than 3* using `
filter` and a lambda.'''

# l=["apple", "an", "cat", "ok"]
# print(list(filter(lambda x:len(x)>3,l))) #['apple']
#----------------------------------------------------------------------------
'''From `[45, 67, 23, 90, 55]`, filter and print only the *passing marks*(greater than or equal to *50*) 
using `filter` and a lambda.'''

# l=[45, 67, 23, 90, 55]
# print(list(filter(lambda x:x>=50,l))) #[67, 90, 55]
#------------------------------------------------------------------------------
'''filter bills greater than 300, add 18% gst using map'''
# l=[120,560,340,890,150]
# g=list(filter(lambda x:x>300,l))
# print(list(map(lambda x:(x*1.18),g))) #[660.8, 401.2, 1050.2]