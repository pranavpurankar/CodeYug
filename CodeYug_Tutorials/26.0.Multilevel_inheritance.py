# Constructor in multi-level inheritance

class Human_being(object):
    def __init__(self):
        print("human being constructor called")
        self.name=input("Enter your name: ")

class Employee(Human_being):
    def __init__(self):
        super().__init__()
        print("Employee constructor called")
        self.salary=float(input("Enter your salary: "))

class Managers(Employee):
    def __init__(self):
        super().__init__(Employee)
        print("Managers constructor called")
        self.bonus=float(input("Enter your bonus: "))

# creating object of employee class
e1=Employee()

# creating object of Managers class
m1 = Managers()