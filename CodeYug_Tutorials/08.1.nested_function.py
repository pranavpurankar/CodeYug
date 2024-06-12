# How nested function works

def outer_function():
    print("This is my outer func")

    def inner_function():
        print("This is my inner function")
    inner_function()

outer_function()

# Create a calculate function, inside this create inner functions which calculates the
# basic arithmetic operations. Little bit tricky example of nested function

def cal():
    def add(a,b):
        return a + b
    def sub(a,b):
        return a - b
    def mul(a,b):
        return a * b
    def div(a,b):
        return a / b
    #we're returning all the values in the form of dictonary
    return {
            "add":add,
            "sub":sub,
            "mul":mul,
            "div":div}
print(cal()["add"](3,5))
print(cal()["sub"](9,3))

print("\nAnother Example of outer & inner function")
# Another example of the inner and outer function

def outer_function_new(x):
    def inner_function(y):
        return y * 2
    result = inner_function(x)
    return result
output = outer_function_new(15)
print(output)

print("\nNested function")
#Triple nested function

def outer_function_outer(x):
    def inner_function_1(y):
        def inner_function_2(z):
            return z**2
        
        return inner_function_2(y * 3)

    result = inner_function_1(x) + x
    return result

result_value = outer_function_outer(3)
print(result_value)
