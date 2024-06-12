'''
Appying multiple decorators one function
'''

# Two decorator
# decor_1 will convert the name into upper case
def decor_1(upper_case):
    def inner():
        return upper_case().upper()
    return inner

# decor_2 will split the name and surname inside list
def decor_2(split_func):
    def inner():
        return split_func().split()
    return inner

# Normal function
@decor_2
@decor_1

def get_name():
    name=input("Enter first name: ")
    surname=input("Enter last name: ")
    fullName=name+" "+surname
    return fullName

print(get_name())