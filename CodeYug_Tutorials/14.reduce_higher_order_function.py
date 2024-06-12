'''
reduce() function: This is built in higher order function defined in 
functool module

Syntax:- 
import functools
functools.reduce(function_name, iterable)

It doesn't return another iterable but returns a single reduced value
'''

# Ex_ Write a function which sums up all and total is nothing but a 
# reduced output
import functools

nums=[5,8,2,10,9]

def func(a,b):
    return a+b

print(functools.reduce(func,nums))

'''
Working of reduce function:
1. It will first pick two elements in the list so we need two arg to define
our function func(). i.e why we took 'a' and 'b' 
    step_1 => 5+8(a+b)= 13
    step_2 => 13+2(a+b)=15
    Like this it will continue till the last value
2. Our result are stored in the reduce 
'''

print("\n\n\n Ex_2_ Find the maximum from the list")
num_max=[5,8,2,9,10,12,36]

def max_num(a,b):
    if a > b:
        return a
    else:
        return b
    
print(functools.reduce(max_num,num_max))
