''''''
'''
create a class student and collect 
id,fname,lname,age,college
create 5 objects
'''

# class student:
#     def setvalue(self,id,fname,lname,age,college):
#         self.id=id
#         self.fname=fname
#         self.lname=lname
#         self.age=age
#         self.college=college
#     def printvalue(self):
#         print(self.id,self.fname,self.lname,self.age,self.college)
# student1=student()
# student1.setvalue('101','A','B',10,'KTU')
# student1.printvalue()
# student2=student()
# student2.setvalue('102','C','D',10,'KTU')
# student3=student()
# student3.setvalue('103','E','F',10,'KTU')
# student3.printvalue()
# student4=student()
# student4.setvalue('104','G','H',10,'KTU')
# student4.printvalue()
# student5=student()
# student5.setvalue('105','I','J',10,'KTU')
# student5.printvalue()
#O/P=============================================
# 101 A B 10 KTU
# 103 E F 10 KTU
# 104 G H 10 KTU
# 105 I J 10 KTU
#-------------------------------------------------------------------------------------------
'''
suppose the college is constant. then we can make it as a static variable
'''
# class student:
#     college='CUSAT'#----------------------> declared the static variable
#     def setvalue(self,id,fname,lname,age):
#         self.id=id
#         self.fname=fname
#         self.lname=lname
#         self.age=age
#     def printvalue(self):
#         print(self.id,self.fname,self.lname,self.age,student.college)#-----------> mentioned the college here
# student1=student()
# student1.setvalue('101','A','B',10)
# student1.printvalue()
# student2=student()
# student2.setvalue('102','C','D',10)
# student2.printvalue()
# student3=student()
# student3.setvalue('103','E','F',10)
# student3.printvalue()
# student4=student()
# student4.setvalue('104','G','H',10)
# student4.printvalue()
# student5=student()
# student5.setvalue('105','I','J',10)
# student5.printvalue()
#o/p==========================================
# 101 A B 10 CUSAT
# 102 C D 10 CUSAT
# 103 E F 10 CUSAT
# 104 G H 10 CUSAT
# 105 I J 10 CUSAT
#-------------------------------------------------

'''
# Task1
# create a class  name Employee
# details -- id , fname , lname , age , prof , loc, company_name  (same company)
# 5 objects
'''

# class employee:
#     company_name='Appollo'
#     def setvalue(self,id,fname,lname,age,prof,loc):
#         self.id=id
#         self.fname=fname
#         self.lname=lname
#         self.age=age
#         self.prof=prof
#         self.loc=loc
#     def printvalue(self):
#         print(self.id,self.fname,self.lname,self.age,self.prof,self.loc,employee.company_name)
#
# emp1=employee()
# emp1.setvalue('101','A','B',25,'C','D')
# emp1.printvalue()
#
# emp2=employee()
# emp2.setvalue(102,'D','E',26,'F','G')
# emp2.printvalue()
#
# emp3=employee()
# emp3.setvalue(103,'H','I',25,'J','K')
# emp3.printvalue()
#
# emp4=employee()
# emp4.setvalue(104,'L','M',26,'N','O')
# emp4.printvalue()
#
# emp5=employee()
# emp5.setvalue(105,'P','Q',25,'R','S')
# emp5.printvalue()

#o/p===================================
# 101 A B 25 C D Appollo
# 102 D E 26 F G Appollo
# 103 H I 25 J K Appollo
# 104 L M 26 N O Appollo
# 105 P Q 25 R S Appollo
#----------------------------------------

'''
# Task 2
# create a class  BankAccount with instance varibles
# acc_no , holder_name , balance
# add a static varible bank name
# create 2 account objects and print their details
'''

# class bankacc:
#     bank_name='SBI'
#     def setvalue(self,acc_no,holder_name,balance):
#         self.acc_no=acc_no
#         self.holder_name=holder_name
#         self.balance=balance
#     def printvalue(self):
#         print(self.acc_no,self.holder_name,self.balance,bankacc.bank_name)
#
# person1=bankacc()
# person1.setvalue(1234,'A','1000')
# person1.printvalue()
#
# person2=bankacc()
# person2.setvalue(1235,'B','1500')
# person2.printvalue()
#o/p==================================
# 1234 A 1000 SBI
# 1235 B 1500 SBI
#--------------------------------------------------------------


'''
# Task 3
# product GST calculation
# create a class product with instance varibale
# name , price
# add static variable gst=18
# write a method to calculate final price = price +(price * gst/100)
'''

class gst_calc:
    gst=18
    def calculation(self,name,price):
        self.name=name
        self.price=price
        return price+(price*(gst_calc.gst/100))
item1=gst_calc()
print(item1.calculation('a',100))


