'''
Exercise 1: Create a function in Python
Write a program to create a function that takes two arguments, name and age, 
and pmerint their value.
'''
print('Exercise_1')

def person_details(name, age):
    print(name, age)


person_details("Pranav", "29")
print('End of Exercise_1\n')

'''
Exercise 2: Create a function with variable length of arguments
Write a program to create function func1() to accept a variable length of
arguments and print their value.

Note: Create a function in such a way that we can pass any number of arguments
to this function, and the function should process them and display each
argument’s value.
'''
print('Exercise_2')


def func1(*args):
    print(args)


func1(20, 40, 60)
func1(80, 100)
func1("pranav", "purankar", "variable length argument")
print('End of exercise_2\n')


'''
Exercise 3: Return multiple values from a function
Write a program to create function calculation() such that it can accept two 
variables and calculate addition and subtraction. Also, it must return both 
addition and subtraction in a single return call.

Given:

def_calculation(a, b):
    # Your Code

res = calculation(40, 10)
print(res)
Expected Output

50, 30
'''

print('Exercise_3')
def calculation(a, b):
    addition = a + b
    substraction = a - b
    return (addition, substraction)


res = calculation(40, 10)
print(res)
print('End of exercise_3\n')



'''
Exercise 4: Create a function with a default argument
Write a program to create a function show_employee() using the following 
conditions.

It should accept the employee’s name and salary and display both.
If the salary is missing in the function call then assign default value 9000
to salary
See: Default arguments in function

Given:

showEmployee("Ben", 12000)
showEmployee("Jessa")
Expected output:

Name: Ben salary: 12000
Name: Jessa salary: 9000
'''
print("Exercise_4")


def showEmployee(name, salary=9000):
    print("Name:",name, "Salary:",salary)


showEmployee("Jessa",12000)
showEmployee("Pranav")
print('End of exercise_4\n')


'''
Exercise 5: Create an inner function to calculate the addition in the 
following way

• Create an outer function that will accept two parameters, a and b
• Create an inner function inside an outer function that will calculate the 
  addition of a and b
• At last, an outer function will add 5 into addition and return it
'''
print("Exercise_5")


def outer_func(a, b):
    def inner_func(a, b):
        return a + b
    add = inner_func(a, b)
    return add + 5


result = outer_func(5, 10)
print(result)
print('End of exercise_5\n')


'''
Exercise 6: Create a recursive function
Write a program to create a recursive function to calculate the sum of numbers
from 0 to 10.

A recursive function is a function that calls itself again and again.

Expected Output:

55
'''
print("Exercise 6")


def recursive_func(num):
    if num:
        return num + recursive_func(num - 1)
    else:
        return 0


res = recursive_func(10)
print(res)
print('Exercise_6 end \n')


'''
Exercise 7: Assign a different name to function and call it through the new 
name

Below is the function display_student(name, age). Assign a new name 
show_tudent(name, age) to it and call it using the new name.
'''
print('Exercise_7')


def display_student(name, age):
    print(name, age)


show_student = display_student
show_student("Emma", 26)
display_student("Pranav", 28)
print('End of exercise_7\n')


'''
Exercise 8: Generate a Python list of all the even numbers between 4 to 30
Expected Output:

[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
'''
print("Exercise_8")


def even_num(start, end):
    even_list = []
    for num in range(start, end):
        if num % 2 == 0:
            even_list.append(num)
    return even_list


print(even_num(4, 30))
print("End of exercise_8\n")


'''
Exercise 9: Find the largest item from a given list
x = [4,6,8,24,12,2]
'''
print("Exercise_9")


def largest_num(number_list):
    number_list = sorted(number_list)
    print('Largest number is: ', number_list[-1])


largest_num([4, 6, 8, 24, 12, 2])

# Another way to solve this, applicable to only list


def max_num(number_list):
    return max(number_list)


print("Largest Number: ", max_num([4, 6, 8, 24, 12, 2]))
print("End of exercise_9\n")
