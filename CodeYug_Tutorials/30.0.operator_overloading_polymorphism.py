'''
Operator Overloading
Python operator overloading refers to a single operator's capacity to perform 
several operations based on the class (type) of operands.
'''
# How operator overloading works internally

print("\n\n int example of operator overloading")
#Ex_ int example

num1=10
num2=20
print(num1+num2)
print(num1.__add__(num2))   #left_operand datatype checked & int based operation
print(int.__add__(num1,num2))   #instead of + used core method
print(int.__dir__) #shows number of methods

'''
Python performs below steps for above operation
step_1 :- check datatype of left operand.
step_2 :- go in that class
step_3 :- call __add__() function
'''

#Ex_ str example

print("\n\nstr example of operator overloading")
str1="hello"
str2="world"
print(str1+str2)
print(str1.__add__(str2))
print(str.__add__(str1,str2))

#==========================================================================
# Achieving operator overloading in python
print("\n\n\nAchieving Operator Overloading\n")

class Book:
    def __init__(self,title,pages):
        self.title=title
        self.pages=pages
    
    def __add__(self,other):    #b1-> self, b2-> other
        total = self.pages+other.pages
        return Book('All books',total)

    def __str__(self):
        return str(self.pages)

b1=Book("One Indian girl",300)
b2=Book("making india awesome",200)
b3=Book("half girlfriend",400)
b4=Book("girl in 105 room",303)

# print("total number of pages: ",b1+b2) => will throw an error
# we want b1+b2 can be achieved -> b1.__add__(b2) we'll create a method
print("total number of pages",b1+b2+b3+b4)


#==========================================================================
# Overloading comparison operator
print("\n\nComparison Operator Overloading\n")

class Hotel:
    def __init__(self,name,fare):
        self.name=name
        self.fare=fare
    def __gt__(self,other): #h1,h2
        return self.fare > other.fare #h1.fare > h2.fare

h1=Hotel('Tajhotel',20000)
h2=Hotel('Panchratn',10000)

print(h1>h2)