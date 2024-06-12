'''
‣ raise keyword
• An exception can be raise forecefully by using the raise clause in python
• raise statement is used when we want to throw exception for particular
  condition.

ex. input age: -10
    ValueError: Invalid age

Syntax:- raise ExceptionName("exception message")
'''


try:
    age = int(input("Enter you age: "))
    if age < 0:
        raise ValueError("Invalid age")
    print("Your age is: ", age)

except ValueError as var:
    print(var)

print("Rest of code")
