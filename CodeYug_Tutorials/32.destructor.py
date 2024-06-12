'''
Refere notes destructor in python
'''

class Employee:

    def __init__(self,nm,sal):
        self.name = nm
        self.salary = sal

    def display(self):
        print(f"Name is: {self.name}\nsalary is:{self.salary}")

    #Defining destructor
    def __del__(self):
        print("desctructor is called")

e1=Employee("Pranav",3690000)
# e1.display()
e2=e1
del e1
