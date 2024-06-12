# Complete OOPs notes are written with the help of excalidraw (ref.Comploops)

'''
Technically, class is a user-defined data type.
        Syntax:
            class Class_name:
                #attributes
                #methods
obj_crea--> obj1 = Class_name([args])
obj_crea--> obj2 = Class_name([args])
'''


# Ex_ Create a class Employee

class Employee:
    def __init__(self, sal, age):
        self.salary = sal
        self.age = age
    pass


e1 = Employee(24000, 5)
e2 = Employee(5698121, 28)
print(e1.__dict__)
print(Employee)


# Topic: Accessing Class Members (Methods, Attributes)

class Organisation: 
    def __init__(self, name, city):
        # Attribute
        self.name = name
        self.city = city

        # Method (function defined inside class)
    def display(self):
        print(f"Org name is {self.name} and city is {self.city}")


org1 = Organisation('Google', 'Pune')

# Accessing attributes outside the class
print(org1.city)
print(org1.name)
org1.city = 'Bengaluru' # updating the city attrib outside the class
print(org1.city)    # print the updated value

# Accessing methods
print(org1.display())

print("\n\nTopic: Built-in class Functions")


class manipulation:
    def __init__(self, nm, ag):
        self.name = nm
        self.age = ag


emp_1 = manipulation('Pranav', 28)
emp_2 = manipulation('Shreyash', 21)

# getattr() func to get the value of attribute


print("The age of employee: ", getattr(emp_1, 'name'))

# setattr() func to change the value of attribute


setattr(emp_1, 'age', 27)
print(emp_1.__dict__)

# deattr() func to delete the value of attribute


print("\nBefore_deleting", emp_1.__dict__)
delattr(emp_1, 'age')
print("After_deleting", emp_1.__dict__)

# hasattr() func check that particular attribute has value or not


print("\nChecking value present or not:-", hasattr(emp_1, 'age'))
print("\nChecking value present or not:-", hasattr(emp_1, 'name'))

# Built-in class attributes
print("\n\nTopic: Built-in class Attributes")


class google_emp:
    # This is details of google employee
    def __init__(self, location, comp):
        self.location = location
        self.comp = comp


g_emp1 = google_emp('Pune', 2700000)
print("\nIt prints the docstring:", google_emp.__doc__)
print("\nEverything present inside class:", google_emp.__dict__)
print("\nIt will print the name of class:", google_emp.__name__)

'''
Checking the instance of the object, which class it belongs to
generally this function is used in the conditionals. If the object
belongs to partcular class perform this operation
'''
print("\n\nisinstance() function")

class demo:
    pass
d1=demo()

print("Is d1 is object of google_emp class: ",isinstance(d1,google_emp))
print("Is d1 is object of demo class: ",isinstance(d1,demo))
