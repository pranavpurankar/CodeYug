'''
Nested class in python
ref OOPS_Python
'''

# Ex_ understanding concept

class Outer:
    def __init__(self):
        print("Outer class constructor called")
    
    def display(self):
        print("This is display method")
    
    class Inner:
        def __init__(self):
            print("Print class constructor called")
        
        def show(self):
            print("This is show method")

obj=Outer()
# Cannot call the inner class directly need to specify the obj of outer class
# and python will check outer class obj then inside that will look for inner cls
inner=obj.Inner()
inner.show()
obj.display()
#You cannot use outer class object to use the inner class method

print("\n\nEx_2")
#Ex_2 

class Student:
    def __init__(self,name,roll,dd,mm,yy):
        self.name=name
        self.roll=roll
        self.dob=self.DOB(dd,mm,yy)
    def display(self):
        print(f"Name is {self.name} and roll is {self.roll}")
        self.dob.display()

    class DOB:
        def __init__(self,dd,mm,yy):
            self.date=dd
            self.month=mm
            self.year=yy

        def display(self):
            print(f"Date of birth is: {self.date}/{self.month}/{self.year}")

s1=Student('Pranav',21,29,11,1995)
s1.display()
