''''''
'''Properties of collection type'''
'''
1----How to define
2----Heterogenous data is supported or not
3----Duplicate values are allowed or not
4----Insertion order preserved or not
5----mutable or immutable'''

'''how to define a tuple'''
''' uses open paranthesis----------- ()------- or we use a function called tuple()
1-- open paranthesis ()
2-- tuple() function
'''
# num=1,2,3
# print(num) #output=(1, 2, 3)
'''if we give random values to a single variable, python considers it as a tuple'''
''''---example--'''
# t=(1,2,3,4)
# print(t, type(t)) #(1, 2, 3, 4) <class 'tuple'>

'''passing a single value to a tuple and see whether it remains as a tuple or not'''
# t=(1) #assigning a single value to a tuple
# print(t,type(t)) #1 <class 'int'> a single value in open paranthesis is not considered as a tuple, but as an integer
'''a single value in open paranthesis is not considered as a tuple, but as an integer'''
'''i want to convert this into a tuple-------add a comma, it gets converted to a tuple'''

# t=(1,)
# print(t,type(t)) #(1,) <class 'tuple'>
'''a single number in open paranthesis is considered as an integer in python'''
'''adding a comma next to that entry makes it a tuple'''

'''Properties of collection type'''
'''
1----How to define
2----Heterogenous data is supported or not
3----Duplicate values are allowed or not
4----Insertion order preserved or not
5----mutable or immutable

'''
'''heterogenous data'''
# t=('a',2,3.5,True)
# print(t,type(t))
#('a', 2, 3.5, True) <class 'tuple'>
#supports heterogenous data

'''Duplicate values are allowed or not'''
# t=(1,1,2,2,3,3,4,4,5,5)
# print(t)
#(1, 1, 2, 2, 3, 3, 4, 4, 5, 5)
#tuple supports heterogenous data

'''Insertion order preserved or not'''
# t=(1,2,3,4,5,6)
# print(t[2]) #3
# print(t[5]) #6
# print(t) #(1, 2, 3, 4, 5, 6) printed as per the given order itself and nothing is altered
# insertion order is preserved as well as indexed

'''mutable or immutable'''
# t=(1,2,3,4,5,6)
# t[1]=5
# print(t[1]) #TypeError: 'tuple' object does not support item assignment
#elements cannot be altered. tuple is immutable

# t=(1 ) # i added space to see whether python treats it as a tuple or integer
# print(t,type(t)) #1 <class 'int'>

''' we can collect the entries from tuple but cannot modify it'''


