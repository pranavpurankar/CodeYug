# Circular referencing
import time


class Employee:
    def __init__(self,obj2):
        self.obj2=obj2

    def __del__(self):
        print("Employee class destructor")


class Account:
    def __init__(self,num):
        self.account_number = num
        self.obj1=Employee(self)

    def __del__(self):
        print("Account class destructor called")


ac = Account(1234)
del ac
time.sleep(5)

# Exception occurs in __init__.Destructor trying to delete the not created thing
# Below program raises an exception if age is negative

class NegativeAge(Exception):
    pass

class Age:
    def __init__(self,ag):
        if ag<0:
            raise NegativeAge("Age cannot be Negative")
    def __del__(self):
        print("Destructor is called")

ag = Age(10)
