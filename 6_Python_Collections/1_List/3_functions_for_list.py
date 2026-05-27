''''''

'''----------------------------
sum()
len()
max()
min()
append()
extend()
-----------------------------'''

'''---------sum()--------------'''

# lst=[1,2,3,4,5,6,7,8,9,10]
# print(sum(lst)) #.....55

'''----------len()-------------:Total number of elements in the list'''
# lst=[0,1,2,3,4,5,6]
# print(len(lst)) #----->7

# lst=[2,4,6,8,10,12,14,16,18]
# print(len(lst)) #---->9

'''------------max()-----------------'''
# lst=[1,2,3,4,5,6,7,8,9,10]
# print(max(lst))  #--->10 prints the max value

'''-------------min()-----------------'''

# lst=[1,2,3,4,5,6,7,8,9,10]
# print(min(lst)) #----> 1 prints the minimum value in the list


'''
# Starting lists
list_a = [1, 2, 3]
list_b = [1, 2, 3]

extra_items = [4, 5]
'''

'''---------------append()--------------------
# Using append
list_a.append(extra_items)
# Result: [1, 2, 3, [4, 5]]  <-- The list is inside the list!
'''

# lst=[1,2,3,4,5]
# extra=[6,7,8,9,10]
# lst.append(100)
# lst.append(extra)
# print(lst) #----------[1, 2, 3, 4, 5, 100 [6, 7, 8, 9, 10]] alist in a list ie: nested list
# for i in lst:
#     print(i,end=' ') #------------1 2 3 4 5 100 [6, 7, 8, 9, 10] the nested list is considered as a single unit in loop


'''-----------------extend()-------------------------'''
'''
# Using extend
list_b.extend(extra_items)
# Result: [1, 2, 3, 4, 5]    <-- The items are flattened out'''

# lst=[1,2,3,4,5]
# extra=[6,7,8,9,10]
# lst.extend(extra)
# print(lst) #-------------[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] it gets merged with the same
# for i in lst:
#     print(i,end=' ') #------------1 2 3 4 5 6 7 8 9 10
#
# lst=[1,2,3]
# lst.extend(5) #doing this results in error
# print(lst)


# lst=[1,2,3,4,5]
# lst.sort(reverse=True) #sort() is an inplace modifier. it doesn't returns a value.
# print(lst) #[5, 4, 3, 2, 1]

'''============================================================='''

'''1 to 15 range elements needs to be added into a list and print that list'''

# lst=[]
# for i in range(1,16):
#     lst.append(i)
# print(lst) #-----[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# lst=[]
# for i in range(1,16):
#     lst.extend([i])
# print(lst)

'''====================================================================='''

'''collect all the even numbers from the range 1-50'''
# lst_odd=[]
# for i in range(1,51):
#     if i%2==0:
#         lst_odd.append(i) '''using append'''
# print(lst_odd)

# lst_odd=[]
# for i in range(1,51):
#     if i%2==0:
#         lst_odd.extend([i]) #using extend
# print(lst_odd)
# print(sum(lst_odd)) #650

'''create a list of elements in the range 1-50 , print the list and its sum. find even and odd nos in the same range and their sum respectively'''

# osum=0
# esum=0
# elist=[]
# olist=[]
# list=[]
# for i in range(1,11):
#     list.append(i)
#     if i%2==0:
#         elist.append(i)
#     else:
#         olist.append(i)
# print(f'The actual list is : {list}')
# print(f'The list of even nos are : {elist}')
# print(f'The sum of even nos are : {sum(elist)}') #-----30
# print(f'The list of off nos are : {olist}')
# print(f'The sum of odd nos are : {sum(olist)}') #-----25

'''======================================================================='''

