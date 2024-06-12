'''
To create user-defined exception we need to follow this steps:
    Step_1.Create exception class and inherit it from Base Exception class
           i.e. Exception
    syntax: class InvalidAge(Exception):
                pass
    
    Step_2.Raise InvalidAge exception for particular condition(age<0) inside
            try block
    syntax: try:
                if age<0:
                    rause InvalidAge("message")

    Step_3. handle the exception using except block.
    syntax: except Exception as obj:
                print(obj)
'''

# Write a python for FiveDivisionError exception. Basically we are trying to 
# create own exception class that throws an exception if we divide by 5.
# There is no built-in FiveDivisionError


class FiveDivisionError(Exception):
    "This is exception class called when five division error happens"
    def __init__(self):
        print("Cannot divide by five")
    pass

# I will write a try block to take input from users


try:
    n1 = int(input("Enter firs number: "))
    n2 = int(input("Enter second number: "))
    if n2 == 5:
        raise FiveDivisionError
    div = n1/n2
    print("Division is: ", div)
except (FiveDivisionError, ZeroDivisionError) as var:
    print(var, end="")
print("rest of code")
