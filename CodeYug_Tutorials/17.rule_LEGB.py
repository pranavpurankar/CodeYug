"""
Before understanding the Closures and Decorators in Python we need to know
Rule LEGB --> Local Enclosed Global Built-In
Mind map --> Inside Built-In => Global | inside Global => Enclosed | inside enclosed Local
                Entire python environ  | Global variable | Not Local Not Global | Local
Always remember it goes from inner to outer
"""

#Revising Local scope

def local_scope():
    x = 20 #local variable
    print(x)

local_scope()

#Global variable
x = 100
def global_scope():
    global x
    x = x+5
    print("GlobalUse: ",x)
    x = 20
    print('LocalVariable: ',x)

global_scope()

#Built-in as name suggest they are reserved one like print

#Non-local variable: This scenario comes when there is nested function

'''
nonlocal a.k.a enclosed scope. Always remember when we have nested
function this scenario arises we want to use the variable.
In a simple sense when we have defined variable inside the outer()
function but not inside the inner() function the variable is neither
local or global hence it is known as non local variable
'''
g = 10 #This is global scope
def outer():
    x = 10 #This is non-local variable
    def inner():
        x = 12 #This is local variable
        print(x)
    inner()

outer()
