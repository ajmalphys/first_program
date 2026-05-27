''''''
'''----------NESTED LIST-------a list comes in a list-----------------'''

# lst=[0,1,[2,3,4],[3,4,5]] # sublists in a main list------its a nested list
# #lets check the index
# print(lst[0]) #0
# print(lst[1]) #1
# print(lst[2]) #[2, 3, 4]
# print(lst[3]) #[3, 4, 5]
#
# #to access an element from a list inside a main list
# print(lst[2][0]) #---2
# #lst[index of the sub list in main list] [index of required element in that sub list]
# #im going to print the second sublist corresponding to index number 3
# print(lst[3][:]) #[3, 4, 5]
# #im going to access the second element in the first sublist [2,3,4]
# print(lst[2][1]) #-----3
# #by using the two square brackets, we can access a list inside a list.


'''---------------------------------------------
create a main list and create nested list. each sub list contains the details of a person consisting of 
ID,first name, last name,age,profession,location, salary'''

# lst=[[1200, 'john','K',20,'driver','aluva',10000],
#      [1201,'jafar','T',21,'Sales','companippady',15000],
#      [1202,'jayan','A',22,'govt','muttom',20000],
#      [1203,'hari','K',23,'engineer','ambattukav',15000],
#      [1204,'devasya','T',24,'film','marine drive',25000],
#      [1205,'das','J',25,'uber','edapally',12000],
#      [1206,'Joy','L',24,'rapido','Kakkanad',20000]]

'''need to print each sublist one by one'''

# for i in lst:
#     print(i)
# print()
# #each sublist contains same number of elements
# #the index of all the first elements in each sublist would be same
# #if i need ID's only
# for i in lst:
#     print(i[0])
# print()
#
# #collect the full detail of persons whose age>22
# for i in lst:
#     if i[3]>22: #i[3]=age in the sublist
#         print(i)

'''incase if one sublist is different in order, then the analysis will not be proper'''

'''collect the details such as f name, l name and age of persons whose age is 24'''
# for i in lst:
#     if i[3]==24:
#         print(i[1],i[2],i[3]) #or print(i[1:4])

'''age>23 and profession rapido. collect their fname, age & location'''

# for i in lst:
#     if i[3]>23 and i[4]=='rapido':
#         print(i[1],i[3],i[5]) #or print(i[1::2])----using slicing

'''find the total salary from the given data'''
# s=[] #--a list to store the salaries from the sub lists
# for i in lst:
#     s.append(i[6])
# print('Total salary is :', sum(s))

