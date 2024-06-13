# This tutorial is incomplete, revise again to understand it

import Student
import pickle


f = open("data.pck", "wb")
n = int(input("Enter number of employees: "))
for i in range(n):
    name = input("Enter the name of employee: ")
    roll = int(input("Enter roll number: "))
    marks = float(input("Enter marks: "))
    obj = Student.Student(name, roll, marks)
    pickle.dump(obj, f)
print("Object store success! ")
