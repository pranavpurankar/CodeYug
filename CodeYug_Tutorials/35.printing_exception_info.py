'''
‣ print Exception name
    1. using exception class object
    2. using sys module
‣ Which exception first?
'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
try:
    div = num1/num2
    print("Division is: ", div)
# If we don't know the name of exception
except Exception as var:
    print(var)
    print(var.__class__)

print("Rest of code")
# ZeroDivisionError: Division by zero


# Example_2
import sys

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

try:
    div = number_1/number_2
    print("Division is:- ",div)
except:
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])

print("Rest of code")
