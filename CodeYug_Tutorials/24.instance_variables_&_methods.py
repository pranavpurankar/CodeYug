# Instance variables and instance methods

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    #This is example of instance method
    #self mein current object ka memory add hojayega
    #the definition of self is conveys the same i.e. current object
    
    def display(self):
        print(self.name,self.marks)
    
    def change_data(self,name,marks):
        self.name = name
        self.marks = marks

std1 = Student('Akshay',89)
std2 = Student('Pranav',93)
std3 = Student('Shreyash',98)

#outside the class creating variables
std1.age=21
print(std1.__dict__)

#creating variable using instance method
std1.change_data('Kapoor',25)
std1.display()

print("\n\nClass Variables")
'''
Class varibales and class methods

Class variables: Class variable is for entire class. 
'''

class employee:
    company_name="Google"

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display_data(self):
        return self.name,self.age,self.company_name
        
    #Class method
    @classmethod
    def get_company_name(cls):
        cls.company_name='Pune Google'
        print(f"Class Method Company name is:",cls.company_name)

emp1 = employee('Pranav',28)
em=emp1.display_data()
print(em)

#How to modify the class variable
employee.company_name='Google India'
emp2 = employee('Shreyash',26)
print(emp2.display_data())

#You can use the object variable to read the class
# variable but cant modify it

emp1.company_name='Google Pune'
print('\nremember this is variable instanstiation: ',emp1.__dict__)
print(emp1.display_data())

#How to access the the class method
employee.get_company_name()

print("\n\n\nSetter and Getter")
'''
setter and getter methods
'''

class employee_details:
    def setName(self,nm): #setter method
        self.name=nm

    def getName(self): #getter method
        print("The name is: ",self.name)

e1 = employee_details()
e1.setName(input("Enter the name: "))
e2 = employee_details()
e2.setName(input("Enter the name: "))
e1.getName()
e2.getName()

print("\n\nStatic Methods")
'''
Static methods
‣ Methods that performs operations external data
‣ It can also perform operations on class data
‣ No need to pass object or class reference
‣ Created using decorator '@staticmethod'

'''

class Bank:
    bank_name = 'BOI'
    rate_of_interest=12.25

    @staticmethod
    def simple_interest(princ,n):
        si=(princ*n*Bank.rate_of_interest)/100
        print(si)


princ=float(input("Enter principal amount: "))
n=int(input("Number of years: "))
Bank.simple_interest(princ,n)