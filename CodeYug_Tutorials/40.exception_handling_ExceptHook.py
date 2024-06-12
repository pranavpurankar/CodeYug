'''
# Traceback:
    If didn't write the code inside the try and except block. If error occurs
    it will return an error inside the traceback.
    
    Traceback provides the more information about the error. It can be helpful
    while looking in the log file. Traceback return info abt current callstack
    status

    Learn more about traceback and callstack

### Before understanding the traceback, 
### what happens when you don't handle an error using try and except block?

- The interpreter calls sys.excepthook() with three arguments.
    i) the exception class
    ii) exception instance/value
    ii) a traceback object

This function prints out a given traceback and exception to sys.stderr

### When does it happens?
- In an interactive session this happens just before control is returned to
  the prompt

Syntax:
Inside sys module
def excepthook(exc_type, exc_value, exc_traceback):
    # prints argument here

### What can we do?
    - We can customize output by overriding this function
    - sys.excepthook() handles uncaught exceptions

Remember your flow still halted it just you can print the good error message

Below is an example I didn't used try and except block so default error msg:

def display():
    print(1 + 'hello')

display()

Traceback (most recent call last):
  File "/home/prns/Downloads/Fundamentals_Database_OS_DataStructures_
  Logarithms_Questions_Networking_FluentPython/Fluent_Python_and_CodeYug_
  Indepth/python_codeyug_indepth/40.exception_handling_ExceptHook.py", 
  line 42, in <module>
    display()
  File "/home/prns/Downloads/Fundamentals_Database_OS_DataStructures_
  Logarithms_Questions_Networking_FluentPython/Fluent_Python_and_CodeYug_
  Indepth/python_codeyug_indepth/40.exception_handling_ExceptHook.py",
  line 40, in display
    print(1 + 'hello')
TypeError: unsupported operand type(s) for +: 'int' and 'str'

'''
import sys  # excepthook()
# below we're modifying this default sys excepthook with format_traceback


def format_traceback(exc_type, exc_value, exc_traceback):
    print("Something went wrong")
    print(exc_type)
    print(exc_value)
    print(tuple(exc_traceback))


sys.excepthook = format_traceback


def display():
    print(1 + "hello")


display()
