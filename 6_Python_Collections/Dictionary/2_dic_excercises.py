''''''
'''create a dic with id,fname,lname,age,prof,loc,salary
check whether the dictionary is iterable or not'''

# d={'id':101,'fname':'sasi','lname':'kumar','age':30,'prof':'police','loc':'kochi','salary':300}
# for i in d:
#     print(i,':',d[i])
#
#
# # print(d.values())
# # print(d.items())
# # print(d.copy())
# print('fname' in d) #membership operator gives boolean output --True
# print('sal' in d) #False
#------------------------------------------------------------------------------------------------------------
'''word count problem using dictionary'''
'''there is a sentence
s='cat rat cat hat rat cat'
output : {'cat':3,'rat':2,'hat':1}
'''
# s='cat rat cat hat rat cat'
# lst=s.split()
# print(lst)
# dic={}
# for i in lst:
#     if i not in dic:
#         dic[i]=1 #t[cat]=1, dic[rat]=1,
#     else:
#         dic[i]+=1
# print(dic) #{'cat': 3, 'rat': 2, 'hat': 1}

#------------------------------------------------------------------------------------------------------------
'''let me add some elements to a dictionary'''

# dic={}
# dic['name']='ajmal'
# print(dic)

#----------------------------------------------------------------
'''# 1. Count how many times each word appears in the sentence
sentence = "Python is simple yet powerful and Python is popular"
# Task: Store each word and its count in a dictionary
'''
# s= "Python is simple yet powerful and Python is popular"
# e=s.replace(' ','')
# print(e)
# w={}
# for i in e:
#     if i not in w:
#         w[i]=1
#     else:
#         w[i]+=1
# print(w)
#-------------------------------------------------------------------
'''
# 2. Store student names and their total marks 
students = {"John": 450, "Arun": 398, "Liya": 470} # Task: Add a new student "Megha" with marks 420 '''

# students = {"John": 450, "Arun": 398, "Liya": 470}
# students['megha']=420
# print(students) #{'John': 450, 'Arun': 398, 'Liya': 470, 'megha': 420}
#--------------------------------------------------------------------
'''# 3. Create a dictionary of even numbers from 2 to 10 and their cubes'''
# dic={}
# for i in range(2,11):
#     dic[i]=i**3
# print(dic) #{2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}
#--------------------------------------------------------------------
'''# 4. You have a dictionary of fruits and their prices: 
fruits = {"apple": 100, "banana": 40, "orange": 80} # Task: Increase the price of banana by 10 '''

# fruits = {"apple": 100, "banana": 40, "orange": 80}
# fruits['banana']+=10
# print(fruits)
#--------------------------------------------------------------------
'''# 5. Store names of countries and their capitals. Then delete one entry 
countries = { "India": "New Delhi", "France": "Paris", "Japan": "Tokyo", "Australia": "Canberra" } 
# Task: Delete the entry for France from the dictionary 
'''

# countries = { "India": "New Delhi", "France": "Paris", "Japan": "Tokyo", "Australia": "Canberra" }
# countries.pop('France')
# print(countries) #{'India': 'New Delhi', 'Japan': 'Tokyo', 'Australia': 'Canberra'}
#--------------------------------------------------------------------
'''# 6. Given a dictionary with names and ages:
 ages = {"Rahul": 21, "Neha": 23, "Arjun": 20} # Task: Find and print the youngest person's name '''

# ages = {"Rahul": 21, "Neha": 23, "Arjun": 20}
# age=min(ages)
# print(age)
#--------------------------------------------------------------------
'''7. Write a program to count character frequencies without considering case (i.e., 'A' and 'a' are the same).
Example: 'ApplEapple' → 'a':2, 'p':4, 'l':2, 'e':2 '''
# s='ApplEapple'
# lo=s.lower()
# print(lo)
# d={}
# l=list(lo)
# print(l)
# for i in l:
#     if i not in d:
#         d[i]=l.count(i)
#     else:
#         pass
# print(d) #{'a': 2, 'p': 4, 'l': 2, 'e': 2}
#--------------------------------------------------------------------



