'''
# Namespace in Python

What are names and Indetifiers in program?
The terms "names" and "identifiers" are often used interchangeably, especially
in programming. They both refer to labels you assign to elements in your code,
but there can be subtle differences in connotation:

Names: In programming, names are often used specifically for variables and 
functions that you create to hold data or perform actions.

Identifiers: Identifiers have a more technical meaning and refer to specific 
strings of characters that uniquely identify an element within a programming 
language.

There are stricter rules for constructing identifiers compared to names in 
general. These rules define what characters are allowed, how long the identifier
can be, and whether it's case-sensitive (e.g., age vs. Age).

Languages enforce these rules to avoid conflicts and ensure clear meaning 
within the code. So, total_price would be considered a valid identifier in 
most languages, following the naming conventions.

Here's an analogy:

Imagine your code as a classroom.
Names are like the nicknames students give themselves (descriptive but not
strictly enforced).

Identifiers are like the official student IDs assigned by the school (unique 
and follow specific formatting rules).
'''

# Ex_1: Names and Indentifiers often used interchangebly

a = 10
print(a)

'''
# What are namespace in the python?
Imagine a giant apartment building. In Python, a namespace is like a floor
in this building. Each floor (namespace) has its own set of unique rooms 
(variables and functions) with different names. This way, you can have a 
room named "living_room" on multiple floors without confusion because they 
are separated by namespaces.

=> Prevents naming conflicts: Namespaces stop variables and functions with the 
same name from clashing with each other.

=> Organization: Namespaces help organize your code by grouping related things
together.

# Types of namespaces #
• Built-in namespace:
Pre-defined functions and objects: It contains all the core functionalities 
that Python offers, like basic mathematical operations, data type conversion,
and commonly used functions.

Always available: You don't need to import anything to use these functions
and objects. They are there by default, ready to be used in any part of your 
code.

Examples: Some common examples of built-in functions include print(), len(),
type(), int(), and str().

You can see available namespace by using dir()
They are just like a dictonary, I am not sure at this movement whether they
are stored in the key value pair or not

• Module level/global namespace: 
In Python, the module-level/global namespace (often referred to interchangeably)
is like a specific floor in your program's giant apartment building. It holds 
variables and functions defined at the top level of your script or module, 
separate from the built-in namespace and local namespaces of functions.

Key Points:

=> Location: 
It exists outside of any functions within the script or module file.

=> Scope:
Variables and functions defined here are accessible throughout the entire 
script or module, but not outside of it (unless explicitly imported).

Example: Imagine you have a script named calculations.py. Any variables or 
functions you define outside of functions in this file belong to the module-
level/global namespace of calculations.py.

• Local namespace: This namespace is for function and classes.
In Python, the local namespace is like your own private apartment within a 
specific floor (module or function) of the giant namespace building. It holds
variables and functions defined within a function, accessible only within 
that function.

Key Points:

Temporary existence: The local namespace is created when a function is called 
and destroyed when the function exits. It's like your temporary living space
during your function's execution.

Scope: Variables and functions defined here are only accessible inside the
function where they are defined. Imagine things you keep in your private 
apartment; you can't access them from outside.

Isolation: This isolation helps prevent naming conflicts with variables or
functions in the global namespace or other functions. It's like having your 
own space without worrying about clashes with neighbors (other functions).

• Enclosed namespace:
The enclosed namespace is a concept that arises when you have nested functions.
It's a specific type of local namespace that exists within another local 
namespace.
'''

# Ex_3 Local Namespace
a=50
def func1():
    a=10
    print("Check for func1:",dir())

def func2():
    a=20

print("Checking local namespace:",dir())

func1()

print("\n\n Enclosed Namespace example")
# Ex_4 Enclosed namespace
# We'll use above example to understand the enclosed namespace
print("Checking GlobalScope: ",dir())
b = 50
def enco_func_1():
    b=12
    def enco_func3():
        e=7
        print("\nChcking Enclosed: ",dir())
    print("\nChecking LocalScope: ",dir())
    enco_func3()
    
def enco_func2():
    b=11

enco_func_1()