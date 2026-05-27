''''''
'''Find all of the numbers from 1–500 that are divisible by 7'''
# l=[x for x in range(1,50) if x%7==0]
# print(l) #[7, 14, 21, 28, 35, 42, 49]
#------------------------------------------
'''Find all of the numbers from 1–300 that have 3 in them---- [3,13,23,30,31,----'''
# l=[x for x in range(1,50) if '3'in str(x)]
# print(l) #[3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43]
#-------------------------------------------
'''list=['apple', 'orange', 'grapes']   convert the list ===> Output: ['APPLE', 'ORANGE', 'GRAPES']'''
# l=['apple', 'orange', 'grapes']
# k=[x.upper() for x in l ]
# print(k) #['APPLE', 'ORANGE', 'GRAPES']
#--------------------------------------------
'''string="Python makes it easy to write powerful and readable code quickly"
5. Count number of spaces in a string
6. Find total number of vowels in a string
7. Find all of the words in a string that are less than 4 letters'''

# s='Python makes it easy to write powerful and readable code quickly'
# print('No: of white spaces are : ',s.count(' ')) # 10
# v='aeiou'
# s1=s.lower()
# l=[x for x in s1 if x in v]
# print(len(l))
# d=s.split()
# print(d)
# c=[x for x in d if len(x)<4]
# print(c) # ['it', 'to', 'and']
#o/p==============================
# No: of white spaces are :  10
# 21
# ['Python', 'makes', 'it', 'easy', 'to', 'write', 'powerful', 'and', 'readable', 'code', 'quickly']
# ['it', 'to', 'and']
#--------------------------------------------------------
'''Create email addresses from names

Question: Use map() and lambda to convert a list of full names into lowercase Gmail addresses 
(firstname + lastname@gmail.com).
Example data:

names = ["Arjun Das", "Meera K Nair", "Vishnu R"]
# Expected → ['arjundas@gmail.com', 'meeraknair@gmail.com', 'vishnur@gmail.com']'''

# names = ["Arjun Das", "Meera K Nair", "Vishnu R"]
# f=list(map(lambda a:a.lower()+'@gmail.com',names))
# print(f)
#['arjun das@gmail.com', 'meera k nair@gmail.com', 'vishnu r@gmail.com']
#---------------------------------------------------------------------------
'''
Abbreviate college names
Question: Convert full college names into uppercase abbreviations using the first letter of each word.
Example data:
colleges = ["National Institute of Technology", 
            "Indian Institute of Science", 
            "College of Engineering Trivandrum", 
            "Government Engineering College Palakkad"]
# Expected → ['NIT', 'IIS', 'CET', 'GECP']'''

# c = ["National Institute of Technology",
#             "Indian Institute of Science",
#             "College of Engineering Trivandrum",
#             "Government Engineering College Palakkad"]
# m=[]
# for i in c:
#     l=i.split() #no need to specify l=[] since the split returns the string as a list.
#     k = ''
#     for j in l:
#         if len(j)>2:
#             k+=j[0]
#     m.append(k)
# print(m) #['NIT', 'IIS', 'CET', 'GECP']
#-----------------------------------------------------------------
'''
 Filter strings starting with a vowel

Question: Filter out only the names that start with a vowel using filter() and lambda.
Example data:

fruits = ["Apple", "Mango", "Orange", "Pineapple", "Avocado"]
# Expected → ['Apple', 'Orange', 'Avocado']'''

# f = ["Apple", "Mango", "Orange", "Pineapple", "Avocado"]
# l=list(filter(lambda x:x[0] in 'aeiouAEIOU',f))
# print(l) #['Apple', 'Orange', 'Avocado']
#-----------------------------------------------------------------------
'''
Capitalize full names

Question: Use map() and lambda to capitalize full names correctly (title case).
Example data:

names = ["rahul r", "deepa menon", "vivek raj"]
# Expected → ['Rahul R', 'Deepa Menon', 'Vivek Raj']'''

# n = ["rahul r", "deepa menon", "vivek raj"]
# l=list(map(lambda x:x.title(),n))
# print(l) # ['Rahul R', 'Deepa Menon', 'Vivek Raj']
#------------------------------------------------------------------------------
'''
Extract domain names from emails

Question: Use map() and lambda to extract only the domain name from a list of email addresses.
Example data:

emails = ["joseph@outlook.com", "anita@gmail.com", "sunil@yahoo.com"]
# Expected → ['outlook.com', 'gmail.com', 'yahoo.com']'''

# e = ["joseph@outlook.com", "anita@gmail.com", "sunil@yahoo.com"]
# l=list(map(lambda x:x.split('@'),e))
# print(l)
# m=[x[1] for x in l]
# print(m) #['outlook.com', 'gmail.com', 'yahoo.com']
#---------------------------------------------------------------------------------
'''
 Filter palindromic words

Question: Use filter() and lambda to return only the palindrome words from the list.
Example data:

words = ["malayalam", "hello", "level", "world", "noon"]
# Expected → ['malayalam', 'level', 'noon']'''

# w= ["malayalam", "hello", "level", "world", "noon"]
# l=list(filter(lambda x:x==x[::-1],w))
# print(l) #['malayalam', 'level', 'noon']
#------------------------------------------------------------------
'''
 Remove special characters

Question: Use map() and lambda to clean up strings by removing special characters 
(only alphabets and numbers).
Example data:

texts = ["he@llo!", "w#orld$", "^python^3"]
# Expected → ['hello', 'world', 'python3']
'''
# t= ["he@llo!", "w#orld$", "^python^3"]
# #here the special characters are within the string itself. if it was on ends, we could have used strip()
# #we should filter each characters based on whether they are alphanumeric or not
# #lets use a filter to do this checking
# #filter(str.isalnum,x) where x is the variable we use inside mapping to iterate in the list
# #str.isalnum checks each character in the string x to return whether its alphanumeric or not
# #if its not, it wont return that particular character. it drops it and doesnt keeps it.
# #each of the alphanumeric character filtered needs to be joined usinh join() method
# #in join, we assign it to an empty string, so it remains as a complete string rather than individual characters.
# #then we need to use map to perform this filtering in each of the elements in the list 't'
# l=list(map(lambda x:''.join(filter(str.isalnum,x)),t))
# print(l) #['hello', 'world', 'python3']
#----------------------------------------------------------------------------
'''
Add hashtags to keywords

Question: Add a # prefix to each word using map() and lambda.
Example data:

keywords = ["python", "datascience", "ai", "ml"]
# Expected → ['#python', '#datascience', '#ai', '#ml']

'''
# keywords = ["python", "datascience", "ai", "ml"]
# l=['#'+x for x in keywords] #-------using list comprehension
# print(l) #['#python', '#datascience', '#ai', '#ml']
# k=list(map(lambda x:'#'+x,keywords)) #-------using map and lambda
# print(k) # ['#python', '#datascience', '#ai', '#ml']
#------------------------------------------------------------------
'''
Filter out empty strings

Question: Use filter() and lambda to remove empty or blank-only strings.
Example data:

lines = ["data", "", " ", "ai", "  ", "ml"]
# Expected → ['data', 'ai', 'ml']
'''

lines = ["data", "", " ", "ai", "  ", "ml"]
l=list(filter(lambda x:x.isspace()==False and len(x)>0,lines)) #condition made in terms of the relevant elements
print(l) #-----['data', 'ai', 'ml']
#
# k=list(filter(lambda x:x.strip(),lines))
# print(k) #-----['data', 'ai', 'ml']
#-------------------------------------------------------
'''Get length of each string

Question: Use map() and lambda to return the length of each string in a list.
Example data:

words = ["machine", "learning", "ai", "model"]
# Expected → [7, 8, 2, 5]'''

# words = ["machine", "learning", "ai", "model"]
# l=list(map(lambda x:len(x),words))
# print(l) #[7, 8, 2, 5]
