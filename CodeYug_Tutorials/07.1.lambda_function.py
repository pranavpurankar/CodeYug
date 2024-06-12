'''
In Python Lambda function is also know lambda expressions, ananomyous function.
A function without name is called lambda function.

They are created using 'lamda' keyword
syntax:-
    lambda arg_list: expression <-- this expression has some rules like
                                    we can't used if else etc there are
                                    other additional rules also present
'''

#How to create lambda function?

add=lambda a:a+10
print(add(20))
'''
Notes: Always remember in the expression part you can't specify the
conditions like and or not or any loops. It should simple python expr
'''

#How we can create a lamda which adds two numbers?

#Normal function
def add_num(a,b):
    return a + b

print("Normal_Func_Output: ",add_num(10,20))

#Now same can be written using lamda function and how to call the lamda func.
#Basically you can't but we can create a alias for the lambda function.

add = lambda a,b:a+b
print(add(1,20))

#Let's say you want to perform both add and substraction using lambda function
add_sub=lambda a,b :(a+b,a-b)
add,sub = add_sub(20,89)
print("add",add)
print("Sub",sub)

#Lets use lamda function with default argument
default_mul=lambda a,b=5:a*b
print(default_mul(5))

print("\n\n'Nested Lambda Functions'")

nested_lamb=lambda x:lambda y:x+y
func_calling_returned_lamb=nested_lamb(30)
print(func_calling_returned_lamb(5))

#Lets understand more clearely by using square function

#This lambda func take numeber as input and returns square of the number
square=lambda n:n**2

'''
1. modify func takes a single argument and lambda func is passed as argument
2. now for lambda function it will create an alias 'func'
3. in return we passed a func alias of square + num
'''
def modify(func):
    num = int(input("Enter a number:"))
    return func(num) + num

print(modify(square))

#Ex_ Now we will be implementing above using lambda function
modifi = lambda funco: lambda num:funco(num) + num
var = modifi(square) #lambda num:func(num)+num
printisi = var(int(input("Enter a number:")))
print("calling_lamb: ",printisi)

print("\n\n IIFE function Immediately Invoked Function Expression")
#In python there is no such concept just I am learning it
print('''
These functions are functions which gets called immediately after the function
      definition. In python we've to use lambda func to make IIFE func
''')
inc=lambda x:x+1

#How to make above function to iffe it is simple

print('Example of IIFE: ',(lambda y:y+3)(5))
print('Example of IIFE: ',(lambda x,y:x+y)(10,20))