#Ex_1: Global and local Variable

def hello():
    x = 3
    print(3)
#print(x)
hello()

print("\n")
#Ex_2 Can both variable have same name? Yes, local and global can have same name. 
y = 5
def same_name():
    y = 3
    print(f"this is my global variable {y}")
    print(3)

print(y)
same_name()

print("\n")
#Ex_3 Modifying global inside the function, by using global keyword.

#This is a global variable
x_global = 5

def greet_global():
    x = 65
    global x_global
    x_global += 1
    print(f"Modifying global variable {x_global}")
    print(f"This is a x variable inside function {x}")
    
greet_global()

print("\n\nGlobalscope- Handling UnboundLocalError: cannot access local variable 'num' where it is not association with a value")
'''
num = 10  #Global variable
def display():
    num = num + 5 #local variable
    num = 20
    print('Inside', num)
display()
print('Outside',num)
'''

print("\nMy expectations from above prorgam is to use global value inside function, and it is not happening. Let's solve this UnboundLocalError")

num = 10
def display():
    global num
    num = num + 5
    print('\nInside',num)

display()
print('Outside',num)

