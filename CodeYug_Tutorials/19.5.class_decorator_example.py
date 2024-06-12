'''
In a previous video we have created a class decorator, lets see an example

Here add function takes 'n' number of arguments and adds them up but the
catch is I want add(10,'20',30) if user passed an string in between input
then our function shouldn't break.

I don't have access to the add function and cannot modify this function so
we need to create an decorator
'''

# We can't modify this function


class Decorator(object):
    def __init__(self, func):
        self.function = func

    def __call__(self, *args):
        try:
            if any([isinstance(i, str)for i in args]):  # [False, True, False]
                raise TypeError("Cannot pass string as argument")
            else:
                self.function(*args)
        except Exception as obj:
            print(obj)


@Decorator
def add(*args):  # *variable length argument
    sum1 = 0
    for num in args:
        sum1 = sum1 + num
    return sum1


print(add(10, 20, 30))
print(add(10, '20', 30))

# add = Decorator()
# add()   # add.__call__()




