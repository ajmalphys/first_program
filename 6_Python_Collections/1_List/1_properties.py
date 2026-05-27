''''''
'''Properties of collection type'''
'''
1----How to define
2----Heterogenous data is supported or not
3----Duplicate values are allowed or not
4----Insertion order preserved or not
5----mutable or immutable

'''

'''1--LIST is defined using square bracket[] or a function called list()
-------------------[] or list()
list() function is used to convert something to a list type
'''
# list=[1,2,3,4,5]
# print(type(list)) #----<class 'list'>
# print(list) #----[1, 2, 3, 4, 5]

# num=1,2,3,4,5
# print(type(num)) #----<class 'tuple'>
# l=list(num) #----converting tuple to list
# print(type(l)) #----<class 'list'>

'''2--hetrogenous data supported or not'''
# lst=[1,2,4,'python',True]
# print(lst) #----[1, 2, 4, 'python', True]----hetrogenous values are supported
# print(type(lst)) #----<class 'list'>

'''3--duplicate values allowed or not'''
# lst=[2,2,'python','python'] #----[2, 2, 'python', 'python']----duplicate values are allowed
# print(lst)

'''4--insertion order preserved or not'''
# lst=[2,2,3,1,4,5,'python']
# print(lst) #----[2, 2, 3, 1, 4, 5, 'python']----insertion order is preserved

'''5--Mutable or immutable
Mutable : can change an element
Immutable : cannot change the elememt

----------------------Index-----------------------
lst=[2,6,7,1,9,10,4]
i want to change 7 to 27
to do that we need to know what index is
each element in the list have an index
it starts from 0 and ends in n-1, where n is the total number of elements in the list
in the current list, there are 7 elements
so our index number varies from 0 --> 6
the first element is 2 & its index is 0
the second element is 6 & its index is 1
similarly............
for 7, index-->2
    1, index-->3
    9, index-->4
    10,index-->5
    6, index-->6
so the index corresponding to 7 is 2
to access a variable from the list, we can do it using this index number
----syntax: lst[2] gives the value corresponding to index:2 which is 7 here

'''
# lst=[2,6,7,1,9,10,4]
# print(lst[2]) #-->7
# #to change it to 27
# lst[2]=27
# print(lst[2]) #-->27 the value has changed to 27 from 7
''' here, using indexing, we changed a value in the list. 
since the change is possible, it is MUTABLE'''

'''
so far we have seen the positive indexing
there is negative indexing also
in negative indexing, the indexing is done from the last value onwards
'''


txt = "My name is Ståle"

x = txt.encode()

print(x)