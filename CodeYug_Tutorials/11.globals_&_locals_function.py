'''
globals() is the in-built function in the python
Symbol table: It is a data structure which contain the necessary information
about global scope of the program.

globals() function returns a dictionary of current global symbol table.
Syntax:- globals()
'''

a = 20
def demo():
    print("'\n'Hello")
    print("\n",globals()['a'])
    #You can change the value inside the symbol table
    globals()['a']=100

    #we can manipulate local variable by using locals function
    b_local = 450
    print("value of local b",locals()['b'])
    print("\n Now changing the value of the local b")
    locals()['b_local']='pranav'
    print('\n Changed value for local()')


demo()
print("\n",globals())
print("\n",a)
