'''
Child class can access the elements of the parents class
But parent class won't access the elements of child class
'''

class Employee:
    bonus=2000
    def display(self):
        print("This is employee class method")

class Manager(Employee):
    bonus1=5000
    def show(self):
        print("This is manager class method")

e1=Employee()
m1=Manager()

print(e1.bonus)

print("\n\nConstructor In Inheritance")
'''
How constructor works in inheritance
‣ By default, constructor of parent  class available to child class
'''

class Father:
    def __init__(self):
        print("Father constructor called")
        self.vechicle='scooter'

class Son(Father):
    pass

s = Son()
print(s.__dict__)


print("\n\nConstructor Overiding")
class Father_1:
    def __init__(self):
        print("Father constructor called")
        self.vechicle="scooter"

class Son(Father):
    def __init__(self):
        print("son constructor priority")
        self.vechicle="BMW"

s=Son()
print(s.__dict__)

# Super Method
print("\n\nSuper Method")

class Computer(object):
    def __init__(self,ram,storage):
        self.ram=ram
        self.storage=storage
        print("Computer class constructor called")

    def display(self):
        print("Hello world")

class Mobile(Computer):
    def __init__(self,ram,storage):
        super().__init__(ram,storage)
        # super().display()
        self.model="iphone X"
        print("Mobile class constructor called")

Apple=Mobile('8gb','512gb')
print(Apple.__dict__)