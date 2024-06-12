'''
Two major use cases :-
    1. In file Handling
    2. In PDBC (Python Database Connectivity)
'''


# Ex - 01
# This code will execute since the file is present if the file name is wrong
# f = open('leetcode.txt', mode='r')

try:
    f = open('leopetcode.txt', mode = 'r')
    # operations
    f.write("Hello world")

except Exception as obj:
    print(obj)
    
else:
    f.close()

print("Rest of code")


# Example 02 Connecting with PDBC
try:
    import mysql.connector

    mysql.connector.connect(
            user = 'root',
            password = 'pranav',
            host = 'localhost',
            port = 3306,
            database = 'student'
            )
except:
    print("Cannot connect")
