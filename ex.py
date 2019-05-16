class Person:

    def __init__(self, name):
        self.name = name
    
    def greeting(self):
        print(f"Hi, my name is {self.name}")

class Student(Person):

    def learn(self):
        print('I get it!')

class Instructor(Person):

    def teach(self):
        print('An object is an instance of a class')
    
nadia = Instructor('Nadia')
nadia.greeting()
nadia.teach()
print()
chris = Student('Chris')
chris.greeting()
chris.learn()

#Create a parent Person class that contains the attribute name and an __init__() method to set the name.
#instructor and student greeting, "Hi, my name is so-and-so". Where's the best place to put this common method?
#Create an instance of instructor whose name is "Nadia" and call their greeting.
#Create an instance of instructor name is "Nadia" and call their greeting.
#Create an instance of student name is "Chris" and call their greeting.
#Call the teach method instructor call the learn student. 
#call the teach method on your student instance. What happens? Why doesn't that work? Leave a comment in your program explaining why.