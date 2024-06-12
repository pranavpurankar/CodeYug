# 3. function as argument
print('\n\n Now lets understand function as argument')

def func():
    print("Hello")

def demo(f):
    f()

def new_func():
    print("I am new function")

demo(new_func)

'''
Lets understand this analogy in a more clear manner
We've two independent function which calculated total salary.
But how one function can interact with another in global space
'''
#Write a two program to calculate the salary with bonus

def Bonus():
    bonus=2000
    return bonus

def total_salary(b):
    basic_salary = 30000
    total_salary = b() + basic_salary
    print("Total Payable salary is: ",total_salary)

total_salary(Bonus)