'''
This tutorial is incomplete, comeback again to understand it

File 45.0, 45.1, 45.2 are part of single example.

This file contains only the attributes and methods of the student class
'''


class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print(f'''Name is: {self.name}\nRoll is: {self.roll}\nMarks is: 
        {self.marks}''')
