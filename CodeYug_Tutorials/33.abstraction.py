from abc import ABC,abstractmethod

# This is your signature and implementation stored somewhere else

class Car(ABC):
    # need to use abstract method
    @abstractmethod
    def mileage(self):
        pass
    
    # concrete method (Normal Method)
    def color(self):
        print("White")

# Since this just an example I am writing an implementation in the same module
# Same module means here right below

class Maruti_Suzuki(Car):
    def mileage(self):
        print("Mileage is 30 kmpl")

class TATA(Car):
    def mileage(self):
        print("Mileage is 35 kmpl")

class Duster(Car):
    def mileage(self):
        print("Mileage is 40 kmpl")
'''
Why we're creating multiple classes for the cars. It is because we cannot create
the object of the Abstract claas. You can't create c1=Car() always keep in mind

‣ How can we call this methods?
  We can call this methods by using the objects of Maruti_Suzuki, TATA, Duster
'''
m1 = Maruti_Suzuki()
t1 = TATA()
d1 = Duster()
m1.mileage()
d1.mileage()
t1.mileage()

'''
What is the real world use case creating signature method and then sub classes
for each vehicle?

'''