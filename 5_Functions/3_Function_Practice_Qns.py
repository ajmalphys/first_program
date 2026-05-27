''''''
'''
Function Practice questions 
-----------------------------

1.Create greeter function
# Define greet(name, lang)
#
# If lang == "en" → Print: "Hello, {name}!"
# If lang == "ml" → Print: "നമസ്കാരം, {name}!"
# If lang == "ar" → Print: "مرحبا، {name}!"

# Try calling the function with different names and language
'''
'''method 1'''
# def greet(name,lang):
#     if lang=='en':
#         print(f'Hello, {name}!')
#     elif lang=='ml':
#         print(f'നമസ്കാരം, {name}!')
#     elif lang=='ar':
#         print(f'مرحبا، {name}!')
# greet('Ajmal','en')
# greet('Ajmal','ml')
# greet('Ajmal','ar')

'''Method 2'''
# def greet(name,lang):
#     if lang=='en':
#         return f'Hello, {name}!'
#     elif lang=='ml':
#         return f'നമസ്കാരം, {name}!'
#     elif lang=='ar':
#         return f'، مرحبا{name}!'
# print(greet('Ajmal','en'))
# print(greet('Ajmal','ml'))
# print(greet('Ajmal','ar'))

'''------------------------------------------------------------------'''
'''
2.Weather Reporter

# Define weatherreport(temp)
# If temp > 30 → print("It's a hot day! Stay hydrated.")
# If 20 <= temp <= 30 → print("Nice and warm outside!")
# If temp < 20 → print("It's a bit chilly today!")
'''
'''Method 1'''
# def wr(t):
#     if t>30:
#         print('It\'s a hot day! Stay hydrated')
#     elif t>=20 and t<=30:
#         print('Nice and warm outside!')
#     elif t<20:
#         print('It\'s a bit chilly today!')
# wr(32) #It's a hot day! Stay hydrated
# wr(25) #Nice and warm outside!
# wr(18) #It's a bit chilly today!.
'''method 2'''
# def wr(t):
#     if t>30:
#         return 'It\'s a hot day! Stay hydrated'
#     elif t>=20 and t<=30:
#         return 'Nice and warm outside!'
#     elif t<20:
#         return 'It\'s a bit chilly today!'
# print(wr(32)) #It's a hot day! Stay hydrated
# print(wr(25)) #Nice and warm outside!
# print(wr(15)) #It's a bit chilly today!


'''--------------------------------------------------------------------------------------'''

'''

3.Grade Evaluator

# Define grade(mark)
# 90-100 → "A"
# 75-89 → "B"
# 50-74 → "C"
# Below 50 → "Fail"
# Print "Your grade is {grade}"'''

'''Method 1'''
# def grade(mark):
#     if mark<=100 and mark>=90:
#         print('Your grade is A')
#     elif mark<=89 and mark>=75:
#         print('Your grade is B')
#     elif mark<=74 and mark>=50:
#         print('Your grade is C')
#     elif mark<50:
#         print('Fail')
# grade(95) #Your grade is A
# grade(85) #Your grade is B
# grade(55) #Your grade is C
# grade(45) #Fail
#
'''Method 2'''
#
# def grade(mark):
#     if mark <= 100 and mark >= 90:
#         return 'Your grade is A'
#     elif mark<=89 and mark>=75:
#         return 'Your grade is B'
#     elif mark<=74 and mark>=50:
#         return 'Your grade is C'
#     elif mark<50:
#         return 'Fail'
#
# print(grade(95)) #Your grade is A
# print(grade(85)) #Your grade is B
# print(grade(55)) #Your grade is C
# print(grade(45)) #Fail



'''4.Fruit Price Checker

# Define fruitprice(fruit)
# If 'apple' → 100/kg
# If 'banana' → 50/kg
# If 'mango' → 120/kg
# Else → "Not available" '''

'''method 1'''
# def fp(f):
#     if f=='apple':
#         print('100/kg')
#     elif f=='banana':
#         print('50/kg')
#     elif f=='mango':
#         print('120/kg')
# fp('apple') #100/kg
# fp('banana') #50/kg
# fp('mango') #120/kg
'''method 2'''
# def fp(f):
#     if f=='apple':
#         return '100/kg'
#     elif f=='banana':
#         return '50/kg'
#     elif f=='mango':
#         return '120/kg'
# print(fp('apple')) #100/kg
# print(fp('banana')) #50/kg
# print(fp('mango')) #120/kg

'''
5.Age Category

# Define agegroup(age)
# age < 13 → "Child"
# 13–19 → "Teenager"
# 20–59 → "Adult"
# 60+ → "Senior Citizen" '''

'''method 1'''
# def age(a):
#     if a<=13:
#         print('child')
#     elif a<=19 and a>=13:
#         print('Teenager')
#     elif a>=20 and a<=59:
#         print('Adult')
#     elif a>=60:
#         print('Senior citizen')
# age(10) #child
# age(15) #Teenager
# age(25) #Adult
# age(70) #Senior citizen

'''method 2'''

# def age(a):
#     if a<=13:
#         return 'child'
#     elif a<=19 and a>=13:
#         return 'Teenager'
#     elif a>=20 and a<=59:
#         return 'Adult'
#     elif a>=60:
#         return 'Senior citizen'
# print(age(10)) #child
# print(age(15)) #Teenager
# print(age(25)) #Adult
# print(age(70)) #Senior citizen



'''6.Area Calculator

# Define area(shape, value1, value2=0)
# If shape == 'circle' → area 
# If shape == 'rectangle' → area 
# If shape == 'square' → area '''

'''Method 1'''

# def area(s,v1,v2=0):
#     if s=='circle':
#         print(f'Area of circle : {3.14*v1*v1}')
#     elif s=='rectangle':
#         print(f'Area of rectangle is : {v1*v2}')
#     elif s=='square':
#         print(f'Area of square is : {v1*v2}')
# area('circle',5) #Area of circle : 78.5
# area('rectangle',5,2) #Area of rectangle is : 10
# area('square',2,3) #Area of square is : 6

'''Method 2'''

# def area(s,v1,v2=0):
#     if s=='circle':
#         return f'Area of circle : {3.14*v1*v1}'
#     elif s=='rectangle':
#         return f'Area of rectangle is : {v1*v2}'
#     elif s=='square':
#         return f'Area of square is : {v1*v2}'
# print(area('circle',5)) #Area of circle : 78.5
# print(area('rectangle',5,2)) #Area of rectangle is : 10
# print(area('square',2,3)) #Area of square is : 6



'''7.Password Strength Checker

# Define checkpassword(password)
# If length < 6 → "Weak"
# If 6–10 → "Medium"
# If > 10 → "Strong" '''

'''method 1'''
# def cp(p):
#     k=len(p)
#     if k<6:
#         print('weak')
#     elif k<=10 and k>=6:
#         print('Medium')
#     elif k>10:
#         print('Strong')
# cp('ajmal') #weak
# cp('ajmalajm') #Medium
# cp('ajmalajmalajmal') #Strong

'''Method 2'''

# def cp(p):
#     k=len(p)
#     if k<6:
#         return'weak'
#     elif k<=10 and k>=6:
#         return 'Medium'
#     elif k>10:
#         return 'Strong'
# print(cp('ajmal')) #weak
# print(cp('ajmalajm')) #Medium
# print(cp('ajmalajmalajmal')) #Strong

'''
8.Language Translator

# Define translate(word, lang)
# If word == "sun" and lang == "ml" → "സൂര്യൻ"
# If word == "sun" and lang == "fr" → "Soleil"
# Else → "Translation not available"
'''

'''method 1'''
# def trans(w,l):
#     if w=='sun' and l=='ml':
#         print('സൂര്യൻ')
#     elif w=='sun' and l=='fr':
#         print('Soleil')
#     else:
#         print('Translation not available')
# trans('sun','ml') #സൂര്യൻ
# trans('sun','fr') #Soleil

'''method 2'''
# def trans(w,l):
#     if w=='sun' and l=='ml':
#         return 'സൂര്യൻ'
#     elif w=='sun' and l=='fr':
#         return 'Soleil'
#     else:
#         print('Translation not available')
# print(trans('sun','ml')) #സൂര്യൻ
# print(trans('sun','fr')) #Soleil


'''picking vowels'''
# n=input('Enter a word')
# for i in n:
#     if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
#         print(i)
'''membership operator
vowels='aeiouAEIOU' '''

'''method 1'''

# vowels='aeiouAEIOU'
#
# def vwls():
#     w = input('Enter word : ')
#     for i in w:
#         if i in vowels:
#             print(i,end=' ')
#     print()
# vwls()
#output------------
# Enter word : aeiou
# a e i o u




'''Method 2'''

# vowels='aeiouAEIOU'
# def vwls(w):
#     for i in w:
#         if i in vowels:
#             print(i,end=' ')
#     print()
# vwls('ajmal') #a a
# vwls('python') #o

'''Method 3'''

# def vowels(w):
#     v='aeiouAEIOU'
#     k='' #declaring an empty string to store the characters
#     for i in w:
#         if i in v:
#             #return i #this return exits the function during the detection of the first vowel itself.
#             k+=i +'\n' #concatenation
#     return k
# print(vowels('Ajmal'))
# print(vowels('aeiou'))
# print(vowels('aeiouAEIOU'))

'''Qn: wap to find the vowel count of a given word'''

# n=input('Enter a word : ')
# v='aeiouAEIOU'
# count=0
# for i in n:
#     if i in v:
#         count+=1
#         print(i,end=' ')
# print()
# print(count)

'''Method 1'''
# def count_vowels():
#     n=input('Enter a word : ')
#     v='AEIOUaeiou'
#     count=0
#     for i in n:
#         if i in v:
#             count+=1
#             print(i,end=' ')
#     print()
#     print(count)
# count_vowels() # a e i o u
#                # 5

'''method 2'''
# def count_vowels(n):
#     v='aeiouAEIOU'
#     count=0
#     for i in n:
#         if i in v:
#             count+=1
#             print(i,end=' ')
#     print()
#     print(f'number of vowles are : {count}')
# count_vowels('aeiou')
#output
#a e i o u
#number of vowles are : 5

'''method 3'''

# def vowel_counter(n):
#     v='aeiouAEIOU'
#     count=0
#     k=''
#     for i in n:
#         if i in v:
#             count+=1
#             k+=i
#     return count
# print(f'The count are : {vowel_counter('aeiou')}')


'''Qn: Temperature converter
write a function : farenheit to celsius(f) that returns temperature in celisius'''

# def temp():
#     n=int(input('click 1 for F-->C and 2 for C-->F : '))
#     if n==1:
#         f=int(input('Enter temp in °F : '))
#         c=(f-32)*(5/9)
#         print('Temp in °C is : ',c)
#     elif n==2:
#         c=int(input('Enter temp in °C : '))
#         f=32+(c*(9/5))
#         print('Temp in °F is',f)
# temp()
#output
# click 1 for F-->C and 2 for C-->F : 2
# Enter temp in °C : 230
# Temp in °F is 446.0



'''Qn: Simple calculator
create functions for add, subract, multiply, divide. then call them based on user input'''

# def add(a,b):
#     return f'Sum={a+b}'
# def sub(a,b):
#     return f'Difference={a-b}'
# def mult(a,b):
#     return f'Product={a*b}'
# def div(a,b):
#     return f'Quotient={a/b}'
# n=input('Select the operation +-*/  : ')
# a=int(input('Enter the first value : '))
# b=int(input('Enter the second value : '))
# if n=='+':
#     print(add(a,b))
# elif n=='-':
#     print(sub(a,b))
# elif n=='*':
#     print(mult(a,b))
# elif n=='/':
#     print(div(a,b))
#output
# Select the operation +-*/  : *
# Enter the first value : 2
# Enter the second value : 3
# Product=6
#-----------------------------
# Select the operation +-*/  : /
# Enter the first value : 10
# Enter the second value : 5
# Quotient=2.0
#-------------------------------
# Select the operation +-*/  : +
# Enter the first value : 5
# Enter the second value : 2
# Sum=7
#-------------------------------

'''Qn: Passsword validator
Create a function that checks if a password is strong (length ≥ 8, contain special character)'''

# def valid(n):
#     l=len(n)
#     sc='/*-+@#$%&()_+'
#     count=0
#     if l>=8:
#         for i in n:
#             if i in sc:
#                 count+=1
#     if count>=1:
#         return 'strong password'
#     else:
#         return 'weak password'
# n=input('Enter a password : ')
# print(valid(n))