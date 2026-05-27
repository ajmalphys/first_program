''''''

'''
.You are given a list of integers, num_list, which represents a consecutive number series. In 
this list: 
There is one repeated number. 
There is one missing number. 
Your task is to write a Python function to: 
• Identify the repeated number. 
• Identify the missing number. 
• Calculate the sum of the repeated and missing numbers. 
Example 1: 
num_list = [1, 1, 3, 4] 
Output: 3 (Repeated number: 1, Missing number: 2, Sum: 1 + 2 = 3) 
Example 2: 
num_list = [1, 2, 2, 4] 
Output: 5 (Repeated number: 2, Missing number: 3, Sum: 2 + 3 = 5) 
Example 3: 
num_list = [2, 3, 3, 5] 
Output: 7 (Repeated number: 3, Missing number: 4, Sum: 3 + 4 = 7)
'''

# l=[2,3,3,5]
# r=[] #list to store the entire nos for reference
# s=l[0] #starting number
# d=0
# n=0 # to store the entry with repetition
# e=l[-1] #ending number
# #since the list is of consecutive numbers, by knowing the first and last elements, we can determine its contents
# print('the first and last values are',s,e)
# for i in range(s,e+1):
#     r.append(i)
# print(r) #prints the reference list
# #now we need to compare the new list with the given list
# for i in r:
#     if i not in l:
#         d=i # stores the missing element
#         break
# print('The missing nuber is : ',d)
# #to find the repeating number
# for i in l:
#     if l.count(i)>1:
#         n=i
# s=d+n
# print(f'Repeated number : {n}--missing number : {d} -- Sum= {n} + {d} = {s}')

# j=set(l)
# k=set(r)
# m=k.difference(j)
# print(m)



'''find how multiple items are removed from a list'''

# l=[1,2,3,4,5,6,7,8,9]
# l[0:5]=[]
# print(l)
