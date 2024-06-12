#Impoted sys to check and set the cout of the recursion
import sys

"""
# Recursion:
In programming, recursion is a way of doing a repetitive task by having a
function call itself.A recursive function call itself usually with a modified
parameter until it reaches to a specific condition. This condition is called
base case. In our earlier examples, the base case would be the smallest Russian
doll or the person at the front of the queue. 

Let's check out an example of a recursive function to understand what we're
talking about. Here, we're defining a function called factorial. At the 
beginning of the function, we have a conditional block defining the base case,
where n is smaller than 2. 

It simply returns the  value 1. After the base case, we have a line where the 
factorial function is calling itself ith n minus 1. This is called the recursive
case.

Real life Example:
1. Russian nested doll (doll inside doll ..)
2. Standing in a queue and don't know the position, then asking a person infront
of you.
This person will ask the next person standing infront of him and this process
goes on till the count reaches first person in the queue.
"""
"""
def factorial(n):
    if n < 4:
        return 1
    return n * factorial(n-1)

print(factorial(3))
"""
def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n-1)
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result

factorial(4)

#Recursion tutorial from CodeYug
print("\nCodeYugRecursion")

#Check recursion limit and change the limit
#to change the limit we will be using sys module
print("Rsr default limit:",sys.getrecursionlimit())
sys.setrecursionlimit(50)
print("Rsr limit is:",sys.getrecursionlimit())

i=0
def demo():
    global i
    i=i+1
    print("Hello",i)
    demo()

print("\nFactorial of N by CodeYug")
'''
#Calculating factorial using recursion
5! = 5

'''

def fact(num):
    if num ==0:
        return 1
    return num*fact(num-1)

print(fact(0))

print("Write a program to find the prime numbers:")
'''
Prime numbers are those who have two divisors only
Ex_ 11 has only two divisors (11, 1)
Decomposion:
    1. Take input name
    2. Input - 1 and check till last number
    3. 
'''


#Below problem is not solved yet

# def prime_num(num,inp):
#     if i ==1:
#         return 1
#     if num%i==0:
#         return 0
#     return prime_num(num,inp-1)

# n=int(input("Enter number: "))
# ind = prime_num(n,n-1)
# if ind==1:
#     print("Prime Number")
# if ind==0:
#     print("Not a Prime number")

def is_prime(n, i=2):
  """
  Checks if a number n is prime using recursion.

  Args:
      n: The number to check for primality.
      i: The current divisor (starts at 2 and increments recursively).

  Returns:
      True if n is prime, False otherwise.
  """
  if n <= 1:
    return False
  if n <= 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False

  # Efficiently check divisibility by 6k +/- 1 up to the square root of n
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i += 6

  return True

# Example usage
number = 113569
if is_prime(number):
  print(f"{number} is a prime number")
else:
  print(f"{number} is not a prime number")
