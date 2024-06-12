'''
What is higher order function in python?
Function which takes other function as arguments. Three Built-in higher order
functions:-

a) filter()
b) map()
c) reduce()

filter() function: This is used to filter out elements of iterable.
Syntax: filter(function_name, iterable)

• function_name:- Function that test every element of iterable. Here we write
                  a logic for selection and removal.

• iterable: sequence which need to be filtered. Sequence like string, tuple, set
            list, from which we have to filter elements.
# True ---> When True the value goes into the filtered object 
# False ---> When False the values gets removed
'''

number=[67,89,56,34,44,20,36,24,14,18,20]

def filter_even(val):
    if val % 2 == 0:
        return True
    else:
        return False
    
output=filter(filter_even,number)
print(output)
print(type(output))

for ele in output:
    print(ele)

print("\n Trying to again use filter obje ele but unable to do")
for i in output:
    print('reusing',i)

'''
Notes:
1. Most important about filter object is once we used the filter object
   it will be vanished. You can't use it again.
2. If you type cast filter object you can use it mutliple times; what 
    it means lets understand using below example. Look in above example
    we used for loop to print every element and we used filter obj
    directly

# Decomposion:
1. So we have data Now passing this data to filter() function
2. Now filter() function don't know what is the logic.
3. So filter function will take another function as argument and inside this
    function we have written our logic, which number should be selected and
    which one should be removed from the list
'''
#Now lets type cast the filter to list; list is preferable bcz it has
#plenty of methods to manipulate data inside it

def filter_odd(val):
    if val % 2 != 0:
        return True

filter_odd = list(filter(filter_odd, number))
print("\n Fitler obj is typecasted: ",filter_odd)

#Now you can reused it lets we want to used it again in for loop
for odd in filter_odd:
    print('\n IteratingAgain:',odd)

#Non zero values
print(bool(None))


print("\n\n Lets try above function using Lambda func")

check_even_odd = lambda num: num%2==0
dato = [10,22,6,8,9,5,7,13]
print(list(filter(check_even_odd,dato)))

