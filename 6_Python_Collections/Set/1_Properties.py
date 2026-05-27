''''''
'''Properties of collection type'''
'''
1----How to define
2----Heterogenous data is supported or not
3----Duplicate values are allowed or not
4----Insertion order preserved or not
5----mutable or immutable'''

'''definition  '''
# s={1,2,3}
# print(s,type(s))

'''heterogenous data is supported or not'''
# s={'a',1,2.3,True}
# l=['a',1,2.3,True]
# t=('a',1,2.3,True)
# print(s) # {1, 2.3, 'a'} unordered and boolean is not supported In your set s = {'a', 1, 2.3, True}, the reason True disappears from the output is that Python evaluates True == 1 as True.
# print(l) # ['a', 1, 2.3, True] ordered and boolean is supported
# print(t) #('a', 1, 2.3, True) ordered and boolean is supported



'''insertion order preserved or not'''
# s={4,3,2,1}
# print(s) #{1, 2, 3, 4} not in the exact order as given in the set


'''duplicate values are allowed or not'''
# s={1,1,2,2,3}
# print(s) #{1, 2, 3} duplicate values are not supported

# s={2,1,4,5}
# print(sum(s)) #12
# s2={2,2,1,4,5} #adding additional '2' which is a duplicate entry.
# print(sum(s2)) #12--- the set ignores that duplicate entry while calculating the sum
# print(max(s)) #5
# print(min(s)) #1
# print(len(s))#4
# print(len(s2))#4

'''mutable or not'''

# s={1,2,3}
# # s.append(4)
# # print(s) #AttributeError: 'set' object has no attribute 'append'


# '''using a method called add(), we can add an element to the set'''
# s.add(4)
# print(s) #{1, 2, 3, 4}
# '''sets are mutable'''

# print(s.add(5)) #none--- why---- add() is an inplace modifier. so it returns none
'''add() is a method--- it can add only a single element at a time'''

'''update() is another method that can be used to add a bunch of elements at a time. its like extend() in lists'''
# s.update([5,6,7]) # use square bracket
# print(s) #{1, 2, 3, 4, 5, 6, 7}
# l=[8,9,10] # its a list and im planning to add it to the set
# s.update(l) # using the update() method for it
# print(s) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10} yes, the set got updated
# t=(11,12,13) #trying to use update to see whether the elemets in a tuple can be added to the set
# s.update(t)
# print(s) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13} yes, the elements in a tuple can also be added to the set
# '''lets try to use add() method to add a tuple to the set'''
# s.add(t)
# print(s) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, (11, 12, 13)} the tuple is added as a tuple inside the set when add() is used

'''remove'''
# s={1,2,3,4,5}
# s.remove(3)
# print(s) #{1, 2, 4, 5}
'''did we checked how to remove multiple elements'''
'''we can do that with pop(), then there is remove() all of these can only remove an element at a time'''
''' check how to remove multiple elemets from a list and set'''

'''discard()'''

'''used to remove an element from a list'''
# s={1,2,3}
# s.discard(3)
# print(s) #{1, 2}
# s.discard(8)
# print(s) #{1, 2} even if the element we are discarding is not there in the set, it doesnt shows any error
# s.remove(8)
# print(s) #KeyError: 8--- if the element is not there in the set, it shows an error

'''the main difference between discard() and remove() is that if we try to remove an element
which is not there in the set, the remove() shows an error while discard() ignores it and doesnt
shows an error'''

# l=[1,2,3]
# #l.discard(2)
# l.remove(2) # [1, 3]
# print(l) #AttributeError: 'list' object has no attribute 'discard'

'''if i try to use discard() with list, it shows an attribute error. it means that discard is specific to set
if i use remove(), it works with both list and set'''

'''---------------------------------------------------------------------------------------------------------'''

