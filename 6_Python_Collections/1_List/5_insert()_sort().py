''''''

'''---INSERT()---'''

# lst=[2,3,4,5,6]
# #------------------index position of 3 is 1
# #------------------i need to add 7 to the position of 3
# lst.insert(1,7)#---first argument is --index-- and second one is the --element-- to be added
# print(lst) #-------[2, 7, 3, 4, 5, 6]

'''---SORT()---'''

# lst=[3,10,0,11,5,9,100,34] # ---------------------a random list, need to sort in ascending order
# lst.sort() #--------------------------------------sorts in ascending order by default
# print(lst) #--------------------------------------[0, 3, 5, 9, 10, 11, 34, 100]
# lst.sort(reverse=True) #--------------------------sorts in descending order
# print(lst) #--------------------------------------[100, 34, 11, 10, 9, 5, 3, 0]

'''...............................................................'''
'''reverse=True------makes the ascending order to descending order'''
'''................................................................'''

'''--------Remove()-------pop()---------'''
# lst=[3,10,0,11,5,9,100,34]#need to remove 10 from this list
# lst.remove(10) # in brackets, give the element in the list to be removed
# print(lst) #--------------------[3, 0, 11, 5, 9, 100, 34]

'''pop() : the index of element should be given in the bracket'''

# lst=[3,10,0,11,5,9,100,34] #need to remove 10 from this list
# lst.pop(1)
# print(lst) #---------[3, 0, 11, 5, 9, 100, 34]


'''what if we dont give any argument in pop()'''
# lst.pop()
# print(lst) #---------------[3, 0, 11, 5, 9, 100]

'''it removes the very last element if we dont pass any index value in pop() function'''

# lst=[3,10,10,10,5,9,100,34] #need to remove 10 from this list
# # i have three 10's in the list
# #let's see whether the remove can remove all 10's
# lst.remove(10)
# print(lst) #---------[3, 10, 10, 5, 9, 100, 34]
# #it doesnt removes the whole 10's
# lst.remove(10)
# print(lst) #------------[3, 10, 5, 9, 100, 34]
# lst.remove(10)
# print(lst) #----------[3, 5, 9, 100, 34]