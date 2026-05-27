''''''
'''Properties of collection type'''
'''
1----How to define
2----Heterogenous data is supported or not
3----Duplicate values are allowed or not
4----Insertion order preserved or not
5----mutable or immutable

'''
'''1----How to define'''
'''
we use curly bracket {} to define dictionary
we enter value as key value pairs
{'key':value}
key should always be in quotes
'''
# p={}
# print(type(p)) #<class 'dict'>
'''let me create a dictionary'''
#dictionary to store---------fname: lname age profession and location
# d={'fname':'ajmal',
#    'lname':'a',
#    'age':30,
#    'profession':'Research',
#    'location':'Kochi'
#    }
# print(d)

'''2----Heterogenous data is supported or not'''
#its heterogenous

'''3----Duplicate values are allowed or not'''
#we need to check both keys and values for duplicates
# d={'name':'anu',
#    'age':26,'mark':20,'mark':50,'mark2':25}
# print(d) #{'name': 'anu', 'age': 26, 'mark': 50, 'mark2': 25} over writing is done with the lase value of duplicate
'''duplicate values are allowed but not keys'''

'''4----Insertion order preserved or not'''
#its ordered

'''5----mutable or immutable'''
# d={'fname':'ajmal',
#    'lname':'a',
#    'age':30,
#    'profession':'Research',
#    'location':'Kochi'
#    }
# d['age']=29 #assigning a new value for the key 'age'
# print(d) #{'fname': 'ajmal', 'lname': 'a', 'age': 29, 'profession': 'Research', 'location': 'Kochi'}
#
# #-------------age is updated and dictionary is mutable--------------

# d['pname']=5 #---------adding something which is not there in the dictionary, will add it to last.
# print(d) #{'fname': 'ajmal', 'lname': 'a', 'age': 29, 'profession': 'Research', 'location': 'Kochi', 'pname': 5}

'''how to remove a value from dictionary'''
# d={'fname':'ajmal',
#    'lname':'a',
#    'age':30,
#    'profession':'Research',
#    'location':'Kochi'
#    }
# d.pop('lname') #removes a key value pair from the dictionary
'''if i want to remove the last item from the dictionary---------popitem()-----'''
# d.popitem() #removes the last key value pair from the list
# print(d) #{'fname': 'ajmal', 'age': 30, 'profession': 'Research', 'location': 'Kochi'}

'''-------clear()------'''
# d={'fname':'ajmal',
#    'lname':'a',
#    'age':30,
#    'profession':'Research',
#    'location':'Kochi'
#    }
# d.clear() #an inplace modifier which clears the dictionary
# print(d) #{}

'''-------popitem()---------'''
# d={'a':1,'b':2,'c':3,'d':4,'e':5}
# print(d.popitem()) #('e', 5)
# d.popitem()
# print(d) #{'a': 1, 'b': 2, 'c': 3, 'd': 4}
