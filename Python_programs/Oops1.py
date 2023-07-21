# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 11:17:50 2023

@author: Administrator
"""
class Person:
    # initializing the variables
    name = ""
    age = 0
    # defining constructor
    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age
        # defining class methods
    def show_name(self):
        print(self.name)
    def show_age(self):
        print(self.age)

# definition of subclass starts here
class Student(Person):
    studentId = ""

    def __init__(self, student_name, student_age, student_id):
        #Person. explicitly calling the person constructor
        #self.name = student_name
        #self.age = student_age
        #instaed of defining the same variables we can use parent constructor variabls
        #as it has same variables
        super().__init__(student_name, student_age)
        self.studentId = student_id

    def get_id(self):
        #print(self.student_name)
        return self.studentId  # returns the value of student id

# end of subclass definition


# Create an object of the superclass
person1 = Person("Richard", 23)
# call member methods of the objects
person1.show_age()
# Create an object of the subclass
student1 = Student("Max", 22, "102")
print(student1.get_id())
student1.show_name()    

