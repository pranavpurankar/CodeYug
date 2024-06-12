'''
Polymorphism in python is according to input object works differently.
'''

# Polymorphism implemented in built in function
# Ex_ len()

len("pranav") #return number of characters #onString
len(['h','e','llo']) #return number of items #onlist

#Ex_ reversed()
emp = ['pranav','shreyash','ram']
company = 'infosys'

for i in reversed(company):
    print(i)

print("\nfor list now: \n")
for i in reversed(emp):
    print(i)

#==========================================================================
print("\n\nChanging built-in functionality")
# Ex_1 Over-riding built-in functions in python

class Cart:
    def __str__(self):
        return "This is cart class object"
c1=Cart()
print(c1)

# Ex_2 

class Cart1:
    def __init__(self,basket1,basket2,basket3):
        self.clothes=basket1
        self.electronics=basket2
        self.other=basket3
    
    def __len__(self):
        print("Total number of intems in cart: ",end="")
        total=len(self.clothes)+len(self.electronics)+len(self.other)
        return total

pranav=Cart1(['pant','shirt','t-shirt'],['iphone','earphone'],['chair'])
print(len(pranav))


#==========================================================================
print('''\n\nExcellent example on polymorphism. According to object passed
        it prints the details\n''')

class BMW:
    def fuel_type(self):
        print("Diesel")
    def max_speed(self):
        print("max speed is 200")

class Ferrari:
    def fuel_type(self):
        print("Petrol")
    def max_speed(self):
        print("max speed is 180")

def car_details(obj):
    obj.fuel_type()
    obj.max_speed()

bmw =BMW()
ferrari=Ferrari()

car_details(bmw)
print("\n----------\n")
car_details(ferrari)

#==========================================================================
print("\n\nPolymorphism with Inheritance\n")

class Veh:
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price

    def get_details(self):
        print("Name: ",self.name)
        print("Color: ",self.color)
        print("Price: ",self.price)
    
    def max_speed(self):
        print("Maximum speed limit is 100")
    
    def gear(self):
        print("gear change is 6")

#Create a car class constructor of Veh would be same for car class
#but max_speed and gear methods to be over-ride for car class

class Car(Veh):
    def max_speed(self):
        print("Maximum speed is 180")

    def gear(self):
        print("gear change is 7")

v1=Veh('Truck','red',200000)
c1=Car('Car','White',180000)

v1.max_speed()
v1.gear()
c1.max_speed()
c1.gear()
