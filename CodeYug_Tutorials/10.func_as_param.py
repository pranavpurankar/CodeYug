'''
Returning function from a function
We can return one function from another function
Important concept for closures and decorators
'''

def outer():
    a = 100

    #It is nested func
    def inner():
        print("Hello world")
    
    return inner
    
    #Above return is for outside function
    '''
    You can't reuturn like this inner() bcz it is func cal
    If you made a call like this it will return none
    because it is function call and it will go back to
    function defition and by default if didn't provided
    return for the function it will return none
    '''

#You can give any name instead of inner.
inner = outer()
inner()

'''
Now lets mix up two concepts:- Taking function as input and 
returning a function as input
Demo func will take input as another function
'''

def display():
    return "Noogler"

def demo(f):
    print(f())
    return f

f1=demo(display)
print(f1())