''''''
'''init is a constructor we use to transfer attributes to a class'''

# class a:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# b=a('ajmal',30)
# print(b.name,b.age)

'''
## *1️⃣ Student Information

Create a class Student with a constructor that takes:

 student name
 age

Create an object and print the name and age using the object.
'''

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=student()