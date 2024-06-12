'''
One decorator function on multiple functions
Division on three values: first two values a,b and then result of a/b 
will be divided by c.
'''
def decor(func):
    def inner(*args): #variable lenght arg will return tuple
        for num in args[1:]:
            if num==0:
                return "cannot divide by zero"
        return func(*args)
    return inner

@decor
def div1(a,b):
    return a/b

@decor
def div2(a,b,c):
    return a/b/c

print("Two args: ",div1(10,5))
print("Three args: ",div2(10,0,5))
print("Two args:",div1(10,0))