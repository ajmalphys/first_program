''''''

'''1.Write a program to find the character that appears the most number of times in a string.
Example: 'banana' → 'a' appears 3 times.'''

# s='banana'
# mc=0 #........................maximum count
# c=0 #.........................count
# e=0 #.........................element with max count
# for i in s: # ................to analyse each element, using a for loop
#     c=s.count(i) #............storing the count of each element in a variable c
#     if c>mc: # ...............an if condition to update the max count
#         mc=c # ...............updating the new max count
#         e=i # ................updating the new element with max count
# #when the program ends, the for loop iterates through all elements and determine the one with max count
# print(f'{e} appears {mc} times')
# #output:
# # a appears 3 times
'''---------------------------------------------------------------------------------------------------------------'''
'''2. Write a program to find the character that appears the least number of times (excluding spaces).
Example: 'mississippi' → 'm' appears once.
'''
# s=' mississippi '
# k=s.strip() #..................strip() removes white spaces from the ends
# print(k) #.....................to see whether the spaces are removed or not
# lc=5 #.........................to update the least count
# c=0 #..........................to update the count
# e=0 # .........................to update the element with least count
# for i in s: # .................to look each entry
#     c=s.count(i) # ............counts and stores the number of occurences of element
#     if c<lc: # ................if the count is less than the min count we set
#         lc=c # ................this updates the min count
#         e=i
# print(f'{e} appears {lc} times')
'''---------------------------------------------------------------------------------------------------------------'''
'''3. find  the longest occurring word  in the list
 lst=['apple' , 'orange' , 'apple' , 'grapes' , 'apple', 'banana']   --- o/p  will be apple  (repeated the most)'''

# lst=['apple','orange','apple','grapes','apple','banana']
# mc=0 #.......................to store the maximum count
# c=0 #........................to store the normal count
# e=0 #........................to store the entry with max count
# for i in lst:
#     c=lst.count(i) #.........counting the number of occurences
#     # print(c)
#     if c>mc: #...............comparing with the max count obtained in previous loop
#         mc=c #...............if the current loop identifies max count, the max count is updated with new value
#         print(mc) #..........printing to see the values stored in mc for diagnostic purpose
#         e=i #................updating the variable e, which holds the entry that corresponds to maximum count
#         print(e)
# print(f'{e} is the most repeated item with {mc} counts')
'''---------------------------------------------------------------------------------------------------------------'''
'''
Check for Duplicate Characters
4. Write a program to check whether a string has duplicate characters or not.
Example: 'unique' → Output: Yes (since 'u' appears more than once)

'''

# s='abbccc' #.........................need to identify the letter that appears more than once
# c=[] #...............................to store the count of each duplicate elements
# e=[] #...............................to store the duplicate entries. using list since the index of entry and count remains same
# for i in s: #........................iterating through each elements in the string
#     if s.count(i)!=1: #..............duplicate means, it appears more than once. so checking for characters with multiple appearance
#         if i not in e: #.............to check whether this element is not in the list of elements (to avoid duplicate entry)
#             c.append(s.count(i)) #...updating the count of that entry in to the list c=[]
#             e.append(i) #............if the element is not in e=[], adding that element to e=[]
# print(c,e)
# for i in range(len(c)):
#     print(f'{e[i]} appears {c[i]} times')
'''---------------------------------------------------------------------------------------------------------------'''
'''
5. Write a program to find the first non-repeating character in a string.
Example: 'swiss' → Output: 'w'
'''

# s='swiss'
# l=0 #..........................declaring a variable to store the first item with no repetition
# for i in s: #..................looping over s to check the count of items
#     if s.count(i)==1: #........non repeating means count=1. checking for those elements
#         l=i #..................storing the non-repeating element when one is found
#         break # ...............since we need the first non-repeating element, break from loop when one is identified
# print(l)
'''---------------------------------------------------------------------------------------------------------------'''


