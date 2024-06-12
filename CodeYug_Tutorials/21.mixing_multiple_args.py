'''
# Mixing multiple types of arguments
1. positional arguments
2. keyword arguments
3. default arguments
4. variable length positional arguments
5. variable length keyword arguments
'''

# we have 
def info(name,age):
    print(name)
    print(age)

info('pranav',age=21)

'''
There are many rules don't need to memorize it but there is order for using
mix arg types. This order is not official one but I learned it from codeyug
This is very useful and valid

positional arg --> variable length positional arg --> keyword arguments -->
variable length keyword arguments --> default arguments
'''

def info_usr(name='N/A', age,city):
    print()