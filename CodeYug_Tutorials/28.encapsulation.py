# Encapsulation in Python

print("Data is accessible")
# Just create a object and data will be accessible
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display(self):
        print(f"name is: {self.name} and salary is:{self.salary}")

prato=Employee("pranav",285000)
# print(prato.__dict__)
print(prato.name)
print(prato.salary)

# =========================================================================

print("\n\nNeed of encapsulation")
# By creating the object of Finance class HR memeber able to manipulate 
# the data inside the Finance class. It not a correct way of doing it.

class Finance:
    def __init__(self):
        self.revenue=10000000
        self.number_of_sales=114

f1=Finance()
print(f1.__dict__)
class HR:
    def __init__(self):
        self.number_of_emp=32
        f1.revenue=21

h1=HR()
print(f1.__dict__)

# =========================================================================

print("\n\nAccess Modifier Privte Member\n")
# Private Member, by adding "__ double underscore" we can make the data memeber
# private.

class Finance_1:
    def __init__(self):
        self.__revenue=12000    #private data
        self.number_of_sales=112
f1=Finance_1()
print(f1.__dict__)

class Hr1:
    def __init__(self):
        self.number_of_emp=21
        # print(f1.__revenue)   #Attribute error

h1=Hr1()
print(f1.__dict__)  #you can't access the private variable

# =========================================================================

print("\n\nAccessing this private members by using methods\n")
# Accessing private members using methods, it is the correct way

class Finance2:
    def __init__(self):
        self.__revenue=10000    #private data
        self.__number_of_sales=112    #private data

    def display(self):
        print(f"revenue is: {self.__revenue} and number of sales: {self.__number_of_sales}")
        self.__revenue=200000
        print(f"revenue is: {self.__revenue} and number of sales: {self.__number_of_sales}")

f2=Finance2()
f2.display()

# =========================================================================

print("\n\nName Mangling\n")
#We know nothing in python is private. You can access the private data by using
#class+obj reference and this concept is know as name mangling. Look at the otput

class Finance3:
    def __init__(self):
        self.__revenue=120000
        self.__number_of_sales=112

f3=Finance3()
print("Name_Mangling",f3.__dict__)
print(f3._Finance3__revenue)

# =========================================================================

print("\n\nCreating Private methods\n")
#We can make any methods private just by adding __ double underscore to it

class Finance4:
    def __init__(self):
        self.__revenue=12000
        self.__number_of_sales=123

    def __display(self):
        print("revenue: ",self.__revenue)
    
f4=Finance4()
print("PrivateMethod:",f4.__display)