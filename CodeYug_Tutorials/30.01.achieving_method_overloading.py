'''
# Achieving Method Overloading in python

We know that if methods with the same name is defined inside the class the 
last method gets executed. 
Instead of defining two methods; one method with some cnoditional logic

class Calci:
    def add(self,num1,num2):
        print("adddition is: ",num1+num2)

    def add(self,num1,num2,num3):
        print("addition is: ",num1+num2+num3)

c1=Calci()
c1.add(10,20)
c2.add(10,20,30)

Below logic is straightforward it up to that programmer, which logic he
chooses. See I am in the basic phase and learning concepts so this are
the building blocks
'''
# Ex_1 

class Calci:
    def add(self,num1=None,num2=None,num3=None):
        if num1!=None and num2!=None and num3!=None:
            print("Addition is: ",num1+num2+num3)
        elif num1!=None and num2!=None:
            print("Addition is: ",num1+num2)
        else:
            print("Incorrent parameters present")

c1=Calci()
c1.add(10,20)
c1.add(10,20,30)

print('\n\nExample 2')
# Ex_2 Calculates the area of square and rectangle


class Area:
    def area(self,length=0,breadth=0):
        if length>0 and breadth>0:
            print("Area of rectangle: ",length*breadth)
        elif length>0 and breadth==0:
            print("Area of square: ",length*length)

a=Area()
a.area(10,20)
a.area(10)