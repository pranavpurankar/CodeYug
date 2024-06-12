'''
Decorators in Python (100% interview question)

The term "decorator" can be traced back to the early days of computer science,
when it was used to describe a type of function that could be used to modify
the behavior of another function. In the context of Python, the term was first
used in the Python Enhancement Proposal (PEP) 222, which was submitted by
Guido van Rossum in 2001. PEP 222 proposed a new syntax for decorators, which
was later adopted in Python 2.4.

The word "decorator" is a good choice for this concept because it captures
the idea that a decorator can be used to "decorate" a function with new
functionality. Decorators are often used to add logging, caching, or other
features to functions without having to modify the code of the functions
themselves.

# CodeYug Simple definition
What is decoration?
Adding things to something to make more attractive/presentable
Ex_ You are giving gift to someone, a gift is watch. You directly won't give
    the watch as it is. You will wrap this gift inside the box and wrapped it
    using gift paper.

# What is decorator in python?
Function which takes other functions as input,add additional functionalities
and return it.
It is a callable python object which modifies other functions/class
Two types of decorator:
    1) Function modifier decorator
    2) Class modifier decorator
'''


# Function modifier decorator


def decor(func):
    def inner():
        # Existing functionality
        func()
        # Additional functionality
        print("Another Welcome: Additional functionality")
    return inner

# Instead of writing like this you can use @ symbol
# printer=decor(printer)


@decor
def printer():
    print('Welcome')
    print('Welcome')


printer()

'''
Decorator function takes another function as input. Below is decomposition
1) decor has local variable called 'func'# Create a closure function
2) when we pass printer as a argument to decor func
3) it will be func inside decor
4) so with func() we can call the printer() function
5) instead of calling the printer func will create a nested func
6) inside nested func we'll add existing functionality that is our printer()
    func you can additional functionality before or after existing functionalit
    dosen't matter
7) you can give any alias for the func call it dosen't matter when the scope is
    not same
'''

# =============================================================================
# Ex_ 2 Write a function which takes input two num and adds them up

'''
New requirement come user wants to add three numbers. You can't change the
existing addition func. Just add the additional functionality using decorator
'''
def deco_add(addition):
    def inner():
        result = addition() # Existing functionality
    
        #Adding additional functionality
        num_3=float(input("Enter third number: "))
        result = num_3 + result
        return result
    return inner


# Normal function without additional functionality
@deco_add
def addition():
    num_1=float(input("Enter first number: "))
    num_2=float(input("Enter second number: "))
    result = num_1+num_2
    round(result,2)
    return result

print("Adding is: ",addition())
