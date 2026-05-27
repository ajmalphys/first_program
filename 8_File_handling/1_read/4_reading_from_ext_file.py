''''''

f=open(r'C:\Users\hp\Downloads\sample.txt','r') #---add 'r' infront to avoid the backslash error

'''Qn:1'''
'''based on this data, do analysis, find age which is equal to 28 and display the details'''
# for i in f:
#     data=i.split()
#     age=int(data[3])
#     if age==28:
#         print(i) #--------------------------102 Meera   Thomas  28  9845012345  Bengaluru
'''if they ask for fname, lname and age'''
        # print(data[1:4]) #------------------['Meera', 'Thomas', '28']
#-------------------------------------------------------------------------------------------------------
'''Qn:2'''
'''loc-chennai-persons's-fname,lname,age and phone number'''

# for i in f:
#     data=i.split()        #---------this split() converts the string to a list
#     if data[5]=='Chennai':
#         print(data[1:5]) #----------------------['Karthik', 'Iyer', '27', '9988776655']
#---------------------------------------------------------------------------------------------------------





