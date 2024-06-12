'''
# Topic: First class function

What are first class objects?
First class objects in a language are handled uniformly throuhtout program.
They can be stored in data structures, passed as arguments, or used in 
control structures.

In python function are treated as first class objects.

Properties of first class functions
1. Function is an object like other objects
2. You can store the function in a variable
3. You can pass the function as a parameter to another function
4. You can return the function from function.
5. You can store them in data structures such as hash tables, lists etc.

Note_1: Python functions supports all this properties; that is why in python 
there is concept of closure and decorators.
'''

'''
Topic: Function as argument | Function as parameter
Two facts:
    1. A function is an object in python
    2. We can create a alias for the function; assigning variable
    Note_2: In python memory is allocated to the objects.
'''

# 1. function as object
def demo():
    print('Hello')
    print('In python memory is allocated to the objects')

#instead of calling function, here I'll try to print the name of function only. You will see there is memory allocation.

#Hence proved function in python worked as an object.
print(demo)

# 2. alias for function

def demo_1():
    print('\n Hello')
    print(''' Here if you observer I have assigned a function reference. new = demo_1. The difference is when we assign the reference we are pointing our new variable to the memoryaddress of function where the function code is stored. In that case we are not calling the function. It is like reference, that is why the code worked. If you want to execute all the instructions inside the function then you've to call the function name followed by parenthesis.
    ''')
#Aliasing function in the new variable
new=demo_1

#Calling function to execute its instruction
demo_1()
new()

