''''''
#syntax
''' var_name=[expression for item in iterable if condition]

method 1
range of elements added into list

method 2
range of elements added into list based on one condition

method 3
range of elements added into a list based on more than one condition


'''

'''method 1
added a range of elements into the list'''
#adding from 1 to 10
# l=[]
# for i in range(1,11):
#     l.append(i)
# print(l)
#syntax for list comprehension
''' var_name=[*content to be in the list* *range*] '''
# lst=[i for i in range(1,11)]
# print(lst)
#------------------------------------------------------
'''Qn: range:20-30'''
# l=[x for x in range(20,31)]
# print(l)
# m=[x for x in range(50,101)]
# print(m)
# n=[x for x in range(1,51)]
# print(n)
# o=[x for x in range(25,46)]
# print(o)
#-----------------------------------------------------------
'''method 2
range of elements added into a list based on one condition
'''
'''
syntax:
var_name=[expression range if condition]'''
#-----------------------------------------------
'''list of even nos in the range 1 to 50'''
# l=[x for x in range(1,51) if x%2==0]
# print(l)
#-----------------------------------------------
'''odd nos in the range 50-100'''
# l=[x for x in range(50,100) if x%2!=0]
# print(l)
#-----------------------------------------------
'''20-45 div by 5'''
# l=[x for x in range(20,46) if x%5==0]
# print(l)
#------------------------------------------------
'''1-50 cube of odd nos'''
# l=[x**3 for x in range(1,51) if x%2!=0]
# print(l)
#------------------------------------------------
'''1-20 sum of eve nos'''
# l=[x for x in range(1,21) if x%2==0]
# print(sum(l))
#-------------------------------------------------
'''1-50 div by 2 and 5'''
# l=[x for x in range(1,51) if x%2==0 and x%5==0]
# print(l)
#------------------------------------------------
'''method 3'''
''' more than one condition'''
'''if else/if elif else'''

'''var_name=[print1 if condition1 else print2 range]'''

'''1-10 square if even and cube if odd'''
# l=[x**2 if x%2==0 else x**3 for x in range(1,11)]
# print(l)

'''
if elif else case
var_name=[print1 if condition1 else print2 if condition2 else print3 range]

we dont explicitly use elif inside list comprehension. instead
we use if else if else pattern. like mentioned in the syntax
'''
#------------------------------------------------------------------------------
'''1-50 even nos cube and odd nos square'''
# l=[x**3 if x%2==0 else x**2 for x in range(1,51)]
# print(l)
#--------------------------------------------------------
'''1-50 range il 
1-15 --> small enn listil varanam
16-35--> medium
36-50--> large'''

# l=[f'{x}:small' if x>0 and x<16 else f'{x}:medium'if x>15 and x<36 else f'{x}:large' for x in range(1,51) ]
# print(l)
#-------------------------------------------------------------
'''wap to count the vowels'''
v='aeiou'
n=input('Enter a string : ')
m=n.lower()
l=[x for x in m if x in v]
print(len(l))
