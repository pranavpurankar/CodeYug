'''
OOP Exercise 1: Create a Class with instance attributes
Write a Python program to create a Vehicle class with max_speed and mileage 
instance attributes.
'''
print("Exercise_1")


class Vehicle_1:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


car = Vehicle_1(80, 19)
print(car.max_speed)
print(car.mileage)
print("End of exercise_1\n")

'''
OOP Exercise 3: Create a child class Bus that will inherit all of the 
variables and methods of the Vehicle class
Given:

class Vehicle

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

Create a Bus object that will inherit all of the variables and methods of the 
parent Vehicle class and display it.

Expected output:
    Vehicle Name: School Volvo Speed: 180 Mileage: 12
'''
print('Exercise_2')


class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


school_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", school_bus.name, "Speed:", school_bus.max_speed,
        "Mileage:", school_bus.mileage)
print("End of exercise_2\n")


'''
OOP Exercise 4: Class Inheritance
Given:

Create a Bus class that inherits from the Vehicle class. Give the capacity 
argument of Bus.seating_capacity() a default value of 50.

Use the following code for your parent Vehicle class.
class Vehicle
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name}is {capacity}passengers"
Expected Output:
    The seating capacity of a bus is 50 passengers
'''
print('Exercise_3')


class Vehicle_2:
 
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passenger"


class Bus_2(Vehicle_2):
    # assigning default value to capacity

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)


school_bus_1 = Bus_2("School Volvo", 180, 12)
print(school_bus_1.seating_capacity())
print('End of exercise_3 \n')


'''
OOP Exercise 5: Define a property that must have the same value for every 
class instance (object)

Define a class attribute "color" with default value white. I.e., Every vehicle
should be white

Use the following code for this exercise

class Vehicle

    def __init__(self, name, max_speed, mileage)
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle)
    pass

class Car(Vehicle)
    pass

Expected Output:
    Color: White, vehicle name: School Volvo, Speed: 180, Mileage: 12
    Coloe: White, vehicle name: Audi Q5, Spedd: 180, mileage: 12
'''
print("Exercise_4")


class Vehicle_3:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus_3(Vehicle):
    pass


class Car_3(Vehicle):
    pass
