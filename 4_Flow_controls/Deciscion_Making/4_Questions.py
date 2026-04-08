'''Qn:1-- input the marks from the user for 5 subjects out of 100 and calculate the total marks
also calculate the percentage and print the percentage
 if percentage is 
 80 and above, grade=A
 70 and below 80, grade=B
 60 and below 70, grade=C
 50 and below 60, grade=D
 below 50,  print 'Failed'''

# s1=int(input('Enter the mark of S1 : '))
# s2=int(input('Enter the mark of S3 : '))
# s3=int(input('Enter the mark of S3 : '))
# s4=int(input('Enter the mark of S4 : '))
# s5=int(input('Enter the mark of S5 : '))
# if s1<=100 and s2<=100 and s3<=100 and s4<=100 and s5<=100:
#     t=s1+s2+s3+s4+s5 #total
#     p=t/5
#     print(f'Total marks: {t} and percentage: {p}%')
#     if p>=80 and p<=100:
#         print('Grade=A')
#     elif p>=70 and p<80:
#      print('Grade=B')
#     elif p>=60 and p<70:
#         print('Grade=C')
#     elif p>=50 and p<60:
#         print('Grade=D')
#     else:
#         print('Failed')
# else:
#     print('Enter marks less than 100')
#there is a problem, if we give mark greater than 100, it accepts

# Enter the mark of S3 : 1000
# Enter the mark of S4 : 100
# Enter the mark of S5 : 100
# Total marks: 1400 and percentage: 280.0%
# Failed
#------------------------------------------------
#i fixed this issue by including an if statement to check whether the given
#--------------------------------------------------
# Enter the mark of S1 : 101
# Enter the mark of S3 : 100
# Enter the mark of S3 : 100
# Enter the mark of S4 : 100
# Enter the mark of S5 : 100
# Enter marks less than 100
#--------------------------------------------------
# Enter the mark of S1 : 60
# Enter the mark of S3 : 50
# Enter the mark of S3 : 70
# Enter the mark of S4 : 75
# Enter the mark of S5 : 45
# Total marks: 300 and percentage: 60.0%
# Grade=C
#--------------------------------------------------


'''Qn:2-- write a program to calculate a persons correct age using their date of birth and current date.
display the correct age
input from the user
birth date
birth month
birth year
current date
current month
current year'''

# dd=int(input('Enter the birth date : '))
# mm=int(input('Enter the birth month : '))
# yy=int(input('Enter the birth year : '))
# cdd=int(input('Enter the current date : '))
# cmm=int(input('Enter the current month : '))
# cyy=int(input('Enter the current year : '))
#
age=cyy-yy
if cmm<mm:
    if
    print(f'{age-1} years, {cmm} months and {cdd} days old')

#
# Enter the birth date : 31
# Enter the birth month : 03
# Enter the birth year : 1995
# Enter the current date : 30
# Enter the current month : 03
# Enter the current year : 2026
# Your are 31 years, 0 months and -1 days old
#-------------------------------------------------------------------
