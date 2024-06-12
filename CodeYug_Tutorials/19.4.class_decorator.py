'''
In python every class is inherited from built-in basic class "object"
If you don't write the object it is by default present.

Class decorator
'''


class Decorator(object):

    def __init__(self, func):
        self.function = func

    def __call__(self, a, b):
        # Original functionality
        result = self.function(a, b)
        # square
        return result**2


# We do not have access to this file it is somewhere else stored on the server


@Decorator
def add(a, b):
    return a + b


# add = Decorator(add)

print(add(1, 2))
