'''
Exception

‣ What is exception?
    Example: 1                  Example: 2
        num1 = 10                   input1 = 100
        num2 = 0                    input2 = "hello"
        result = num1/num2          result = input1 + input2
        print(result)               print(result)
        .   .   .                   .   .   .
        .   .   .                   .   .   .
        ("Rest of code not be executed.After error for both")
        
        o/p:                        o/p:
        ZeroDivisionError           TypeError

    • An exception is an event which occurs during the execution of program
      that disrupts normal flow of program.
    • Situation that python can't cope with it.

‣ Need of exception handling   
  
  Why it is Dangerous?
    • Lead to sudden termination of program
    • Can block the application
    • Data loss problem can occur.
    • Corrupt data files.

‣ Exceptions vs Syntax Error
    • Errors cannot be handled
    • Exceptions can be handled using exceptions handling syntax
    ex: print("print)

Exception Handling
• try block
• except block
• else block
• finally block

In python every exception is a class.

Syntax:
    try:
        # Code containing exceptions (suspicious code)

    except [ExceptionName]:
        # Code to handle exceptions(if occurred)

    else:
        # Code to execute if no exceptions
    {either one of block that is except or else will be executed not both}

    finally:
        # Always executed ()
    {else and finally blocks are not mandatory}
'''


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

try:
    div = num1/num2
    print(di)
except (ZeroDivisionError, NameError) as obj:
    print(obj)
# except NameError:
# print("Variable name is wrong")

print("rest of code")


# When you aren't sure about the exceptions then you can simply write only
# except: and print("Something went wrong") but not a good dev practise


# Example_2: else and finally block


number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
# We write the code that is suspicious inside the try block
try:
    div = number_1/number_2
    print(div)
except:
    print("Something went wrong")
else:
    print("an exception didn't occur")
# we close file or database connection in finally block (general use)
finally:
    print("Always executed")
print("rest of code")
