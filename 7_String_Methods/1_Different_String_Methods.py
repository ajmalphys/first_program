''''''

'''
we can find the length using len()
1--len(),,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
s='python'
length=len(s)
here len() is a  function. it takes a value in

METHODS

--------count()--------
to count the number of items in a string'''

# s='apple'
# # print(count(a)) this doesnt work. it is not a function, but a method
# print(s.count('a')) #1

# lst=['apple','grapes','apple','kiwi','apple'] # a list
# #using count to determine the count of an entry
# print(lst.count('apple')) #---3

s='apple'
d=[1,2,3,4]
print(len(s))

'''in methods, we use dot operator, in functions, we dont use dot operator'''

'''--------index()---------'''
# s=('pythonn')
# print(s.index('y')) #--1
# print(s.index('o')) #--4
# # print(s.index('a')) #value error
# print(s.index('n')) #--5 it displays the index of first element if there are duplicates
# print(s.count('n')) #2

'''--------title()--------'''
'''used to capitalize each sentence'''
# s='ajmal learns python'
# print(s.title()) #---Ajmal Learns Python
# print(len(s)) #--19
# print(s.count('a')) #--3
# print(s.index('p')) #--13

'''------------swapcase()----------'''
'''to swap cases, ie; upper and lower cases'''
# s='PythoN'
# print(s.swapcase()) #---pYTHOn ---it swaps capital to small and small to capital
# t=('AjMaL')
# print(t.swapcase()) #---aJmAl

'''------------capitalize()----------'''
# s='python'
# print(s.capitalize()) #----Python----- the first letter is changed to its capital version
# t='ajmal is learning python'
# print(t.capitalize()) #Ajmal is learning python----- only the first letter is capitalized
# u='ajmal Is Learning Python'
# print(u.capitalize()) #---Ajmal is learning python---

'''-----------------upper()----------------------'''
# s='python'
# print(s.upper()) #PYTHON

'''-----------------lower()------------------------'''
# s='PYTHON'
# print(s.lower()) #---python
# t=s.lower() #python
# print(s,t) #PYTHON python

'''------------------isalpha()--------------------'''
''' it means isalphabetic
it checks whether a string is alphabetic or not
it returns a boolean value, whether it is true or not'''

# s='python'
# t='!@thon'
# print(s.isalpha()) #----True
# print(t.isalpha()) #----False it doesnt supports numerics and special characters
# u='python python' #inserted space
# print(u.isalpha()) #---False---- it doesnt supports space between characters
# v='python_python'
# print(v.isalpha()) #---False---- specail character (underscore) is not considered

'''-----------------isalnum()-----------------------'''
''' is alphanumeric----- checks whether the string is alphanumeric'''

# s='python123'
# print(s.isalnum()) #True
# t='python'
# print(t.isalnum()) #True
# q='p ython'
# print(q.isalnum()) #False---------spaces are not considered
# w='!@thin'
# print(w.isalnum()) #False----------speacial characters are not allowed


'''--------------isdigit()-----------------------------
checks whether the string is digit or not'''

# s='123'
# print(s.isdigit()) #True
# q='a123'
# print(q.isdigit()) #false

'''------------------replace()---------------------'''
'''to replace some thing'''

# s='python developer'
# #need to change python to java
# print(s.replace('python','java')) #---java developer
# t='123 123'
# print(t.replace('1','5')) #523 523

'''---------------------strip()-----------------------'''
''' used to remove---what?------ to remove white spaces from the ends'''
# s='p y t h o n'
# print(s.strip()) #p y t h o n-----------the spaces inb/w are not removed
# q=' p y t h o n '
# print(q.strip()) #----p y t h o n--------removed space from end and beginning
'''if we want to remove something specific like a character from the ends, then we can mention that element int he strip fn'''
# e='@python'
# print(e.strip('@')) #python
'''------------lstrip() and rstrip()----------------'''
'''
lstrip()----------- removes spaces from the left
rstrip()-------------removes spaces from the right'''

# r='@python@'
# print(r.lstrip('@')) #--------python@
# print(r.rstrip('@')) #-------------@python
# print(r.strip('@')) #--------------python
# #w3schools.com/python/python_ref_list.asp

