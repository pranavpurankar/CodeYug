'''
Types of Recursion:-
1) Direct Recursion: When a function calls itself, it means calling function
    inside the function defition.

2) Indirect Recursion: A function calls another function which then calls the
    first function again
'''

# Ex_1 Direct recursion
# Write a program for printing n to 1 sequence

num = int(input("Enter the value: "))

def dec_num(num):
    print(num)
    if num ==1:
        return 1
    return dec_num(num-1)

dec_num(num)

'''
Common template for recursion problems, we can solve recusrsion problems using
below template.

def rec_func():
    base cond:
        return
    #Code
    return [recursive call i.e. rec_func()] #recursive case 
'''

# Ex_2 Indirect recursion
# Function calls another function

def num(n):
    if n <=0:
        return
    print(n,end=" ")
    num_1(n-1)

def num_1(n):
    print(n,end=" ")
    num(n-1)

num_1(10)