''''''
#instance variable
''' 
we are creating a class persons, we need to collect the info about that person
fname, lname and age, location
'''

class Person:
    def setvalue(self,fname,lname,age,loc):
        #self came as default
        self.fname=fname #these are instance variable, we can use this variable in other methods
        self.lname=lname
        self.age=age
        self.loc=loc

    def printvalue(self):
        print(self.fname,self.lname,self.age,self.loc)
#collecting the details
person_1=Person()
person_1.setvalue('Ajmal','A,'30','kochi')
person_1.printvalue()

person_2=Person()
person_2.setvalue('Rabiya','PA',29,'kochi')
person_2.printvalue()


