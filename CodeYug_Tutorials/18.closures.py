'''
Closures in python is important function
Pre-requisite:
    # 1.Function as object: We know that every function is object in python. 
        Function is a class and if check the type of function it says 
        <class 'function'> it means every func is obj
    
    # 2.Nested function: Funtion defined inside the function. To call inner 
        function we make the call from outer function scope
    Ex:
        def outer():
            print("Hello")
            def inner():
                print("Bye")
            inner()
        outer()

    # 3. How function works (Taking above example)
        * When python interpreter comes to line 10, it gets func definition
        * Until we call function it won't be executed but it will create a
            namespace for outer func.
        * On line 15 func called interpreter will go back to line 10
            and then value assignment carried out if any variable with value is 
            present.
        * Once everything is done memory will be free up by removing all the values
            and everything. This is done by garbage collector.
        * Remember that actual values are stored inside the memory and variable
            name are the indefiers/name of that value which points to the actual
            value in the memory
        Like this function will be executed I didn't included every minute step
        in the function defition.
    
    # Aliasing function
        I can give the alias to the function. We know that function name without
        () represents the object. It means name of above function outer represent
        the object and we can assign it to new variable
        ex_ new = outer
            new()
        still outer function is executed
'''
# Closures in Python
'''
Closure: 
A closure is a function that remembers and has access to variables in the local
scope even after the outer function that created it has finished executing. 
It's like the inner function is "enclosing" the outer function's local variables
and carrying them with it.
'''
# Below is the normal nested function 

def outer():
    def inner():
        x=200
        return x
    inner()


print("This is nested func",outer())

# Now returning with function call


def outer_func():

    def inner():
        a = 369
        return a
    return inner()  #Here returning function call


print("This is return with func call: ",outer_func())
# Now instead of function call we'll return function object

def outer_func_obj():
    def inner():
        roush = 369
        return roush
    return inner

new = outer_func_obj()
print("This func call will return obj: ",new())

# You can give the nested function name to the alias as the nested function
# has local scope and now you can create a global alias of that func

inner = outer_func_obj()
print("This is an alias of func: ",inner())

'''
Now we understood the logic behind this but what is closure

line_73 => python interepreter will see a function defition and for this it will
            create a namespace. In that namespace it will add inner function only

line_79 => Called a function, interpreter will go inside the outer_func_obj def
            It will create local namespace for inner() func.

line_76 => Return 'roush' this value will be returned to the point from where
            the function is called. So it will return to 'inner' obj inside
            outer_func_obj function.

line_77 => Return 'inner' this value will return to 'new' because function is
            called from there.

Once it executed the line 85 everything means memory allocated to the function
it's data will be deleted. Nothing is present in the memory.

So how we are getting the final output or value of 'roush' ie 369?
The idea is, value gets attached to the code, even if the value is not present
in the memory and that is the concept of closure.
Value is being attached to the code in our case 369
'''

#Two definition of closure by codeyug:
'''
• Closure is a technique by which data gets attached to the code.

• Closures are function objects that remebers value in the enclosing scope
even if they are not present in the memory.
'''
