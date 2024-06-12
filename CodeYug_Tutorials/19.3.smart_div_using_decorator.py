
def smart_divisor(f):
    def inner(num1,num2):
        if num2 == 0:
            print("Cannot divide by zero")
            return
        f(num1,num2)
    return inner

@smart_divisor
def division_func(num1,num2):
    print("Division is: ", num1/num2)

division_func(10,0)
division_func(5,9)