'''
What is Fibonacci series?
The Fibonacci series is a special series of numbers where each number is 
simply the sum of the two numbers before it. It starts with 0 and 1, and
then you just keep adding!

Here's an example:

    Start with 0 and 1 (0, 1)
    Next number is 0 + 1 = 1 (0, 1, 1)
    Then 1 + 1 = 2 (0, 1, 1, 2)
    And so on: 2 + 1 = 3, 3 + 2 = 5, etc. (0, 1, 1, 2, 3, 5)

The series keeps going forever, with the numbers getting bigger and bigger.
It's a neat pattern found in nature and even math puzzles!
'''

# Ex Fibonacci
def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return (fib(n-2) + fib(n-1))

n = int(input("Enter number of terms: "))
for i in range(1,n+1):
    print(fib(i))