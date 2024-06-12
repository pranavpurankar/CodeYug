print("#==== Hierarchical Inheritance ====#\n")
# Hierarchical Inheritance

# Person :- name, age   => Parent
# Student :- marks      => child_1
# Employee :- salary    => child_2

class Person:
    def __init__(self,nm,ag):
        self.name=nm
        self.age=ag
    def display(self):
        print('This is person display method')

class Employee(Person):
    def __init__(self,nm,ag,sal):
        self.salary=sal
    def display1(self):
        print('This is Employee display method')

class Student(Person):
    def __init__(self,nm,ag,m):
        super().__init__(nm,ag)
        self.marks=m
    def display2(self):
        print('This is Student display method')

s1=Student('Shreyash',23,90)
e1=Employee('pranav',28,145000)
p1=Person('Nikhil',31)

# s1.display1() #It will give attr-error(child_1 cannot access child_2 propr)
# ====================================================================

print("\n\n#==== Multiple Inheritance ====#\n")

class Country:
    def __init__(self):
        print("Country class constructor")
        self.Office="Delhi"

class State:
    def __init__(self):
        super().__init__()
        print("State class constructor")
        self.Office='Mumbai'

class District(State,Country):
    def __init__(self):
        super().__init__()
        print("District class constructor")
        self.Office="Pune"

d=District()
print(d.__dict__)