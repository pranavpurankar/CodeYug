'''
Reutrn statement in python
'''
# Ex: Write a function to calculate the simple interest

'''
Formula of SI = PrincipaAmout * InterestRate * Time / 100
'''

#Take three variable to store below values

p = 10000
r = 12.25
t = 3

def simple_interest(p,r,t):
    si = int((p*r*t)/100)
    print("Simple interest is: ", si)
    return si

si = simple_interest(p,r,t)
print(si)
total_pay = p+si
print('Total payment: ',total_pay)

# Suppose I want to use the SI variable outside the function,
# Let's say I want to add principal amount to si it's not possible as the scope of si is local
# So in this cases we need to use the 'return keyword or statement'
# Return keyword will return the value to the function call


print("\n\n Earlier in the return example we returned single value; Now w'll return multiple values")

# Ex: Add and substract two numbers and return them
def add(a,b):
    sum1 = a+b
    sub = a-b
    return sum1,sub

result = add(2,3)
print(result)
print(type(result))

'''
When we return multiple values using the return keyword in python.
The data type of this values is tuple. It is comma separated means
tuple. You can do 'tuple unpacking' it means we can assign the 
variable in the order to a values in tuples.
'''

# Ex: Now we will store the value directly in two variable

def mul_div(c,d):
    mul = c * d
    div = c / d
    return mul,div

mul1, div1 = mul_div(4,8)
print(mul1)
print(div1)
