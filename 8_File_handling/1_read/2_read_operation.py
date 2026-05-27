''''''
'''
var_name=open(file_name/path,mode_of_operation)

if the file comes in the same directory just pass the file name in  syntax 
if not, we need to give the path of the file. file name is not sufficient in that case
'''

'''create a reference'''
# f1=open('File_handling_read_reference','r')
# print(f1) #<_io.TextIOWrapper name='File_handling_read_reference' mode='r' encoding='cp1252'>
#the output is in an encoded manner. its not an error
# i want to list it out one by one
# for i in f1:
#     print(i)
#output---------------------------------------------------------------
# this is not a python file
# this is a normal file
# lets add some data
# data science
# data analyst
# java
# testing
# flutter
# lets read the courses from this using read operation using python
'''--------------------------------------------------------------------------------------------------------'''
# f2=open('read_ref_2','r')
# for i in f2:
#     print(i)
#output---------------------------------------------------
# Ajmal
# Panayappilly House
# HMT colony
# Kalamassery
'''---------------------------------------------------------------------------------------------------------------'''
'''till now we did  it from the same directory itself

lets try to do it from a different diretory'''

# f3=open('C:\Users\hp\PycharmProjects\first_program\8_File_Handling_Dir2\read_ref1','r')
# for i in f3:
#     print(i)
# '''SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape'''
# '''this erro suggests that we read the path, but the trucated error indicatees the slashes are backward in the file path '''
# '''change the backward slashes to forward slashes'''

'''
how to copy the file path
go to the file we plan to read in the directory, right click, select copy filepath/reference. from the box that appears
select the absolute path
'''

# f=open('C:/Users/hp/PycharmProjects/first_program/8_File_Handling_Dir2/read_ref1','r')
# for i in f:
#     print(i)

# from another package
# Ajmal
# Panayappilly House
# HMT colony
# Kalamassery
#--------------------------------------------------------------------------------------------------------------

