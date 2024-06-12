'''
gemini ai definition:
In Python, a partial function is a function derived from an existing function with a predetermined set of arguments. It's created using the partial function from the functools module.

CodeYug definition
Partial function allows us to fix a certain number of arguments of a function
and generate a new function.

Syntax of partial:
parital(func, arg1, arg2...)
'''
# from functools import partial
# def add(n1,n2,n3,n4):
#     return n1+n2+n3+n4

# new_fun = partial(add,2,3)
# print(new_fun(5,10))

'''
Whenever you create a partial function always use keyword length it is not a
rule but to avoid positional arg clashing with keyword
'''

# Now create a function with keyword argument
#Instead of importing complete functool module we'll import only partial

from functools import partial   #noqa 402

def add(n1,n2,n3,n4):
    return n1+n2+n3+n4

new_add=partial(add,3,6)
print(new_add(10,5))