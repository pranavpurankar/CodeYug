# This is revision on python by ineuron


# Ex_1.check whether the number is even or odd

def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")


number = 3
check_even_odd(number)

# Ex_2 Find the factorial of the number
# Formula => n! = n x (n-1) x (n-2) x (n-3)....1


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result = result * i
        return result


number = int(input("Enter a number to calculate it's factorial: "))
result = factorial(number)
print(f"The factorial of {number} is: {result}")
print("\n")

# Ex_3 Arithmetic Operation using python


def calculate(a, b, operation):
    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result == a * b
    elif operation == 'divide':
        if b != 0:
            result = a / b
        else:
            result = "Cannot divide by zero"
    else:
        result = "Invalid operation"
    return result


num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
op = input("Provide the operation (add, substract, multiply, divide): ")

result = calculate(num1, num2, op)
print(f"Result: {result}")
