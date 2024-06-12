'''
Types of arguments in python
1) Positional Arguments
2) Keyword arguments
3) Default arguments
4) Variable length arguments
    There is two subtypes:
    a) Variable length arguments
    b) Variable lenght keyword arguments
'''

#1.Positional Arguments

print('\n1. Positional arguments, order matters and number of arguments must be equal to parameters')

def pow(a,b):
    print(a ** b)

print(pow(2,3))

# 2.Keyword Arguments
print('\nKeywords arguments. ref. python_theory.txt')

def info(name,age):
    print(f"name is {name} and age is {age}")

info(age=28, name='pranav')

# 3.Default Arguments
print('\nDefault Arguments. We explicitly writes the value in the parameter')

def default_func(orgnisation="Google", employee_id=52):
    print(f'The name of company is {orgnisation} and employee id is {employee_id}')

default_func()

# There are some rules while passing positional or defaults arguments
# Positional arguments follow keywords arguments. It means we can't pass keyword arg followed by positional argument.
'''
def throw_error(name='Pranav',age=21):
    print(f"The name is {name} and age {age}")

throw_error(name="Shreyash", 21)
'''

# If you passed the keyword arguemnts follow positional arg. It will work

def key_follows_pos(name="Pranav", age=28):
    print(f'My name is {name} and age is {age}')

key_follows_pos('pranav', age=25)

print('\nVariable lenght arguments')
print('They are of two types: 1. Variable length arg 2.Variable keyword length arg')

# Let's we want to pass multiple arguments to the parameters. Want to make the function dynamic. It means as per need number of arguments will change. Ex: Sometime user will pass 4 args, sometimes 5 arg or any number of args as per need So we will user variable length arguments.

# Below function is an example of simple positional arguments
def sum1(num1, num2, num3):
    print(num1+num2+num3)
sum1(10,20,30)

# We want to make above function dynamic. User can pass any number of args and function will return the sum of all elements

print('''\n
        Now we want to make the function more dynamic. Dynamic means if user
        wants to add multiple number they can perform this operation by passing
        multiple input as args to the func parameters.
        Ex sum(10,20); sum(10,20,30)
        ''')

def sum_all(*nume):
    sum=0
    print(type(nume))
    for i in nume:
        sum = sum+i
    print(sum)

sum_all(10,20)
sum_all(10,20,30,40)
sum_all(10,20,30,40)

print('''
        Lets understand the working of the above function
        1. declared a function with multiple parameter by using * and variable
        nume
        2. When interpreter reaches the call sum_all(10,20)
        3. The control passess to the function definition and values will be
        store in the tuple. Why tupple, because whenever we use *asteriks it
        will create a tuple and this tuple is stored in local variable nume.
        4. Initialized the sum=0 variable
        5. For loop will iterate through each value and i as element will add
        sum to the variable sum after each iteration
        6. Once iteration is completed it will print the final result stored
        in the sum variable
        ''')


print('''
        Now there is slight change in above program:
        If we declared a parameter in the func def.
        ''')

def new_sum(n,*num):
    print('Checking_type num',type(num))
    sum = 0
    for number in num:
        sum = sum + number
    print(f'The sum is {sum}')

new_sum(10,20)
new_sum(10,20,30)
new_sum(10,20,30,40)

print('''
        Explanation of above code:
        1. Interpreter sees a function definition
        2. Now interpreter comes to the called function
        3. Here, n is the first positional argument, so the first value in arg
        always asign to 'n'. Hence we're seeing -10 for each sum. After this
        intepreter will come to *num and store all the values after 10 in the
        tuple.
        We know the next flow.
        ''')

print('''
        \nVariable length keyword arguments
        In this we pass a arguments with keywords. We use double ** asterisks
        fllowed by variable name to use variable length keyword arguments.
        In the parameter it will assigned to a dictonary in the form of key,
        value pair
        ''')

def variable_keyword(**numo):
    print('Checking_Type_numo',type(numo))
    sum = 0
    for key in numo:
        sum = sum + numo[key]
    print(sum)

variable_keyword(num1=10,num2=20, num3=30)

print('''
        \n What happens when we add positional parameter.
        Our code will only add the number passed to the variable length
        parameter variable.Because as per the mechanism first argument is
        assigned to the first parameter
        ''')

def additional_param(n, **multiple_args):
    sum = 0
    for value in multiple_args:
        sum = sum + multiple_args[value]
    print(sum)

additional_param(n=10, n1=20, n2=30, n3=40)

