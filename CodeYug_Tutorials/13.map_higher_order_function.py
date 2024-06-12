'''
Map () function: This is built in higher order function. It apply a 
specified function on each element of the iterable and perhaps change
element

Syntax:- map(function_name,iterable)
Remember: 1) The map object can be consumed only once.
2) Multiple arguments can be passed to the map function.
'''

#Ex_1 Write a program to find the square of each number in list
nums = [3,6,9,2]

def square(num):
    return num*num

mapped=map(square,nums)
print(type(mapped))
#Advantage of using list is we can use multiple functions in the list
print(list(mapped))

#Now implement the same logic using lambda function
lambo=lambda num: num*num
map_lambo=map(lambo,nums)
print("Lambda_Output:",list(map_lambo))
print("Consume_Once: You'll get empty",list(map_lambo))

print("\n\n\n Another Example")
'''
Ex_2 Mapping between multiple iterables
Add two list using map function
'''
num1 = [10,20,30]
num2 = [1,2,3]

#Output should be 11,22,33

'''
add1 function:
a will take one input as arg from num1
b will take one input as arg from num2
This logic can be varied
'''
def add1(a,b):
    return a+b

mapo=list(map(add1,num1,num2))
