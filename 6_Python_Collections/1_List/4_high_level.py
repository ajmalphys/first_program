''''''

'''Qn:1--wap to find the armstrong number from the given range 100-500'''
'''153=(1^3)+(5^3)+(3^3)
1534=(1^4)+(5^4)+(3^4)+(4^4)'''

# lst=[]
# for i in range(100,501):
#     q=0
#     z=i
#     for k in range(3): #------assigning z to i so that z can be manipulated in the nested for loop
#         p=z%10
#         q=(p**3)+q
#         z//=10
#     if q==i:
#         lst.append(i)
#     else:
#         pass
# print(lst) #-------------------------------------------[153, 370, 371, 407]
# print(f'Largest armstrong number is : {max(lst)}')
# print(f'Largest number is : {lst[-1]}') #--------------407
# print(f'second largest number is : {lst[-2]}') #-------371
# print(f'Third largest number is : {lst[-3]}') #--------370
#---------------------------------------------------------------------------------------------
'''Qn.2 : Harshad (Niven) number'''
'''A number that is divisible by the sum of its digits'''

#how i can use list for harshad numbers
#print and store the harshad numbers in a range

# lst=[]
# l=int(input('Enter the lower range: '))
# u=int(input('Enter the upper range : '))
# ll=len(l)
# lu=len(u)
# for i in range(l,u+1):
#---------------------------------------------------------------------------------------------
'''Qn.3 : Perfect number'''
''' A number whose sum of proper divisors (excluding itself) equals the number'''
''' example : 6--- 
Divisors : 1,2,3
1+2+3=6
so 6 is a perfect number
if not equal, print Not a perfect number'''

#---------------------------------------------------------------------------------------------
'''Qn.4 : Strong Number
   A number whose sum of factorials of digits equals the number.
   Example: 145
   1! + 4! + 5! = 1 + 24 + 120 = 145
   So, 145 is a Strong number.
   If not equal, print Not a Strong number.'''
#---------------------------------------------------------------------------------------------
'''Qn:5 lst=[1,3,4,6,10,2]
need to create a new list from the given list.
the elements in the new list should be the square of its positions. eg: lst=[1**1, 3**2, 4**3, 6**4, 10**5, 2**6]'''

# lst=[1,3,4,6,10,2]
# lst2=[]
# count=1
# for i in lst:
#     k=i**count
#     count+=1
#     lst2.append(k)
# print(lst2) #[1, 9, 64, 1296, 100000, 64]

'''based on index'''
# lst=[1,3,4,6,10,2]
# lst1=[]
# j=1
# for i in range(len(lst)):
#     lst1.append(lst[i]**j)
#     j+=1
# print(lst1)
'''Does string have index?'''
# a='ajmal'
# print(a[2])  #-->m-----indexing works with strings
# print(a[0]) #-->a

'''string is iterable
it have index
'''
#---------------------------------------------------------------------------------------------
'''Qn:6  Ask the usr for a number and check if the given number is present in the given list or not
if element is found print, 'element is found', if not, print ' element not found' '''

# lst=[1,2,3,4,5,6,7,8,9,10]
# n=int(input('enter a number : '))
# count=0
# for i in lst:
#     if i==n:
#         count+=1
#     else:
#         continue
# if count!=0:
#     print('Element found')
# else:
#     print('Element not found')

'''using membership operator'''

# lst=[1,2,3,4,5,6,7,8,9,10]
# n=int(input('Enter a number : '))
# if n in lst:
#     print('Element found')
# else:
#     print('Element not found')
#---------------------------------------------------------------------------------------------
'''Qn:7  generate [35,47,40,44,41,43] from lst=[15,3,10,6,9,7]'''

# lst=[15,3,10,4,9,7] #the list to be generated is obtained while subtracting the individual elements from 50
# lst2=[]
# for i in lst:
#     lst2.append(sum(lst)-i)
# print(lst2)
#---------------------------------------------------------------------------------------------
'''Qn:8  lst=[1,1,1,2,3,4,4,5,6,7,3,8,11,23,11,45] remove the duplicates and create a clean list'''
# lst=[1,1,1,2,3,4,4,5,6,7,3,8,11,23,11,45]
# lst1=[]
# for i in lst:
#     if i in lst1:
#         continue
#     else:
#         lst1.append(i)
# print(lst1)

# lst=[1,1,1,2,3,4,4,5,6,7,3,8,11,23,11,45]
# lst1=[]
# for i in lst:
#     if i not in lst1:
#         lst1.append(i)
# print(lst1)
#---------------------------------------------------------------------------------------------
'''Qn:9  wap to create a list of words and find all words that starts and end with same letter. 
store the words in a new list and print both the new list and the total count of such words'''

# l=['dad','mom','son','rose','bulb','blue','malayalam']
# l2=[]
# for i in l:
#     if i[0]==i[-1]: #using negative indexing to access the last character in a word
#         l2.append(i)
# print(f'The given list is : {l}')
# print(f'The elements with same starting and ending letters are : {l2}')  #['dad', 'mom', 'bulb', 'malayalam']
# print(f'The number of elements in the new list are : {len(l2)}')
'''----------another way to do it------------------------------'''
# l=['dad','mom','son','rose','bulb','blue','malayalam']
# l2=[]
# for i in l:
#     k=len(i)
#     if i[0]==i[k-1]: #using negative indexing to access the last character in a word
#         l2.append(i)
# print(f'The given list is : {l}')
# print(f'The elements with same starting and ending letters are : {l2}')  #['dad', 'mom', 'bulb', 'malayalam']
# print(f'The number of elements in the new list are : {len(l2)}')
'''-----------------------------------------------------------------------------------'''
'''Qn:10  Largest prime number from the range of 50 -->200'''
# lst=[]
#
# for i in range(50,201):
#     count = 0
#     for j in range(2,i):
#         if i%j==0:
#             count+=1
#     if count==0:
#         lst.append(i)
# print(lst)
# print('The largest prime among the given range is : ',max(lst))
#---------------------------------------------------------------------------------------------
'''Qn:11  Largest harshad number from the range 1-->500'''
# lst=[]
# for i in range(1,501):
#     sum=0
#     k=str(i)
#     temp=i
#     for j in range(len(k)):
#         sum=sum+(temp%10)
#         temp//=10
#     if i%sum==0:
#         lst.append(i)
# print(max(lst))
#-----------------------------------------------------------------------------------------------
'''Qn:12 largest fibanocci number below 1000'''
# lst=[1,1]
# a=1
# b=1
# c=2
# while c<1000:
#     a=b
#     b=c
#     c=a+b
#     if c<1000:
#         lst.append(c)
# print(lst)
# print(max(lst))
#----------------------------------------------------------------------------------------------
'''Qn:13 wap to find the largest number b/w 100 and 1000 whose first and last digit are same'''

# lst=[]
# for i in range(100,1001):
#     k=str(i)
#     if k[0]==k[-1]:
#         lst.append(k)
#     else:
#         continue
# print(max(lst))
#---------------------------------------------------------------------------------------------
'''Qn:14 wap to find largest odd palindrome number in range 100-->500'''

# lst=[]
# odd=[]
# for i in range(100,501):
#     rev = ''
#     k=len(str(i))
#     temp=str(i)
#     for j in temp:
#         rev=j+rev
#
#     #print(rev)
#     if rev==temp:
#         lst.append(temp)
#
# print(lst)
# for i in lst:
#     if int(i)%2!=0:
#         odd.append(i)
# print(odd)
#---------------------------------------------------------------------------------------------
'''Qn:15 wap to find the largest perfect number b/w 1-100'''

''' A number whose sum of proper divisors (excluding itself) equals the number'''
''' example : 6--- 
Divisors : 1,2,3
1+2+3=6
so 6 is a perfect number
'''

# lst=[]
# for i in range(1,101):
#     sum=0
#     for j in range(1,i):
#         if i%j==0:
#             sum+=j
#
#     if sum==i:
#         lst.append(i)
# print(lst)
# print(f'Largest perfect number is : {max(lst)}')
#---------------------------------------------------------------------------------------------
