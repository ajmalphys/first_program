''''''
'''
OOPs-object oriented programming
---------------------------------
why we are using oops?
1--reusability
2--inheritance
3--encapsulation


oops = class + object + reference

class:
they are blueprints/base model

object:
they are instances of a class

reference: 
operations to be done from the object
-------------------------------------------------------------
# class -- blueprint / base model
# object -- instance of class
# reference -- mode of opertions to be done


# class - car
# object - kia , thar , bmw , benz----
# reference --- drive , stop , start , accelerate


#class - TV
#object -- LG , sony , samsang , ----
#reference -- watching , vol up , down


#class - bike
#object -- bullet , duke , honda , yamaha ,-----
#reference -- riding ,


first we need to create class.
how to create a class

syntax:
-----------------
class class_name :
-----------------
Note: while naming class, follow the rules for identifiers.
------------------------------------------------------------
*--its better to start class name with capital letter
-------------------------------------------------------------
'''

# class student:
#     pass #need t give something inside. we cannot keep the body of the class empty
# class Student:
#     pass #this is another class since  identifiers are case sensitive
#----------------------------------------------------------------------------------

class book:
    def method_1(self):  #------------self:instance keyword---------
        print('reading book 1')
    def method_2(self):
        print('reading book 2')
    def method_3(self):
        print('reading book 3')
#created 3 methods, we defined a class
#this is not an object yet
#let's create an object
#pass a name for the object
#---------------------------------------
obj_1=book() #iwant to access method_1
obj_1.method_1() #reading book 1
#--------------------------------------
obj_2=book()
obj_2.method_2() #reading book 2
#----------------------------------------
obj_3=book()
obj_3.method_3()  #reading book 3
#---------------------------------------
obj_4=book()
obj_4.method_3()    #reading book 3
obj_4.method_1()    #reading book 1
#-----------------------------------------



