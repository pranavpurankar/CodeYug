"""
There are two types of decorators: User defined and Built-in decorators
There are many built-in decorators. But below three decorators are used
quite useful: @classmethod @statismethod @property

Need of property decorator?

The property decorator in Python is a built-in function that allows you
to create properties. A property is a special type of object attribute
that can be accessed like a regular attribute but has additional functi
onality.

The property decorator takes three arguments:
‣ A getter function: This function is called when the property is accessed.
‣ A setter function: This function is called when the property is assigned
  a new value.
‣ A deleter function: This function is called when the property is deleted.
  The getter, setter, and deleter functions are optional. If you do not
  provide a getter function, the property will be read-only. If you do not
  provide a setter function, the property will be write-only. If you do not
  provide a deleter function, the property will not be deletable.

class Employee

    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname
        self.mail = firstname + lastname + "@gmail.com"

    def fullname(self):
        return f"{self.first} {self.last}"


e = Employee("pranav", "purankar")
e1 = Employee("rajendra", "chavhan")
e2 = Employee("aman", "dattarwal")

e.first = "simran"
print(e.first)
print(e.mail)
print(e.fullname())

Here is catch you changed the lastname but mail is still printing
the old value. The self.mail and self.first are independant; so 
even after changing the value self.mail is printing old value.
Below I have used property decorator; but before that what if
we create a new method for this. You can but when objects are many
it is not possible to add obj.mail() to every object. If you look at
the out put it printed the objects location in the memory.
"""


class Employee:

    def __init__(self, firstName, lastName):
        self.first = firstName
        self.last = lastName
        # self.mail = firstName + lastName + "@gmail.com"

    @property
    def mail(self):
        return f"{self.first}{self.last}@gmail.com"

    @property
    def fullname(self):     # getter method
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split()
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None


e = Employee("pranav", "purankar")
e1 = Employee("shreyash", "purankar")
e.first = "simran"

print(e.fullname)
print(e.mail)
e.fullname = "Virat Kohli"

print("\nAfter setting")
print(e.fullname)
print(e.mail)
print(e.first)
print(e.last)

print("\nAfter deleting")
del e.fullname
print(e.first)
print(e.mail)
print(e.last)
