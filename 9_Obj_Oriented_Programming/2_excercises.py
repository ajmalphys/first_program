''''''
#im going to create a class called humans
#what are the features of humans--- hearing, speaking, running, walking

# class Human:
#     def sight(self):
#         print('Human can see')
#     def hear(self):
#         print('Human can hear')
#     def speak(self):
#         print('Human can speak')
#     def walk(self):
#         print('Human can walk')
#     def run(self):
#         print('Human can run')
# #these are blueprint
# #its not yet an object. lets create an object, or a human
#
# anu=Human() #creating an object from class
# anu.sight() #Human can see
# anu.hear()  #Human can hear
# anu.speak() #Human can speak
# anu.walk()  #Human can walk
#
# print('*'*100)
#
# #creating another human
# ajmal=Human()
# ajmal.sight() #Human can see
# ajmal.speak() #Human can speak
# ajmal.hear() #Human can hear
#
# print('*'*100)

#basically we are reusing the code here.


'''
create a class, make objects, and call methods.

Task 1 - Car

Create a class `Car` with the following methods:

* `start()` -> "Car started."
* `drive()` -> "Car is moving."
* `stop()` -> "Car stopped."

Requirements:

* Create an object `car1` and call all the methods in order.
* Create another object `car2` and call only the `drive()` method.

---
'''
# class car:
#     def start(self):
#         print('car started')
#     def drive(self):
#         print('car is moving')
#     def stop(self):
#         print('car stopped')
# car1=car()
# car1.start()
# car1.drive()
# car1.stop()
# print('*'*100)
# car2=car()
# car2.drive()


'''
Task 2 - Mobile Phone

Create a class `Mobile` with the following methods:

* `call()` -> "Calling someone..."
* `message()` -> "Sending a message."
* `camera()` -> "Taking a photo."

Requirements:

* Create an object `phone1` and call all three methods.
* Create another object `phone2` and call only `camera()`.

---
'''

# class mobile:
#     def call(self):
#         print('calling someone')
#     def message(self):
#         print('sending a message')
#     def camera(self):
#         print('taking a photo')
# phone1=mobile()
# phone1.message()
# phone1.call()
# phone1.camera()
# print('*'*100)
# phone2=mobile()
# phone2.camera()

'''
Task 3 - Animal

Create a class `Animal` with the following methods:

* `eat()` -> "Animal is eating."
* `sleep()` -> "Animal is sleeping."
* `make_sound()` -> "Animal is making a sound."

Requirements:

* Create an object `dog` and call all methods.
* Create another object `cat` and call only `eat()` and `make_sound()`.

---
'''
# class animal:
#     def eat(self):
#         print('animal is eating')
#     def sleep(self):
#         print('animal is sleeping')
#     def make_sound(self):
#         print('Animal is making a sound')
# dog=animal()
# dog.eat()
# dog.sleep()
# dog.make_sound()
#
# print('*'*100)
#
# cat=animal()
# cat.eat()
# cat.make_sound()
#
# print('*'*100)

'''
Task 4 - Teacher

Create a class `Teacher` with the following methods:

* `teach()` -> "Teaching the class."
* `check_homework()` -> "Checking homework."
* `conduct_exam()` -> "Conducting an exam."

Requirements:

* Create an object `teacher1` and call `teach()` and `conduct_exam()`.
* Create another object `teacher2` and call all three methods.
'''


# class teacher:
#     def teach(self):
#         print('teaching the class')
#     def check_homework(self):
#         print('checking home work')
#     def conduct_exam(self):
#         print('conducting an exam')
#
# teacher1=teacher()
# teacher1.teach()
# teacher1.conduct_exam()
#
# print('*'*100)
#
# teacher2=teacher()
# teacher2.conduct_exam()
# teacher2.teach()
# teacher2.check_homework()
#
# print('-'*100)


'''
Task 5 - Robot

Create a class `Robot` with the following methods:

* `greet()` -> "Hello, human!"
* `dance()` -> "Robot is dancing."
* `sing()` -> "Robot is singing."

Requirements:

* Create an object `robot1` and call all methods.
* Create another object `robot2` and call only `greet()` and `sing()`.
'''

# class robot:
#     def greet(self):
#         print('hello human')
#     def dance(self):
#         print('robot is dancing')
#     def sing(self):
#         print('robot is singing')
# robot1=robot()
# robot1.sing()
# robot1.dance()
# robot1.greet()
#
# print('-'*100)
# robot2=robot()
# robot2.greet()
# robot2.sing()