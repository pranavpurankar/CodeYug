'''
Shallow Copy stores the copy of the original object and points the references to the objects.
the wrong way of copying is by using assignment operator
ex mylist = newlist X don't do this copying
Copying can be done by using copy module
'''
#Why never use a '=' assignment operator for copying
mylist = [10,20,30,40,50,60]
print(f'Mylist{mylist}')
print('Id of mylist:',id(mylist))
newlist = mylist
print(f'\nNewlist{newlist}')
print('Id of newlist:',id(newlist))

print('\nWhen we change the duplicated list, it wil also change the original list items')
newlist[0]=99
print(f'Changed 0th value in newlist{newlist}')
print(f'Changes also happened in mylist{mylist}')
print('Id of newlist',id(newlist))
print('Id of mylist',id(mylist))

print('''
        \n Shallow Copy Tutorial
        Shallow copy can be done using shallow copy module.
        It will create a  new tag and new memory allocation.
        But still if we change the duplicated list, the changes
        are made to the orignal list too.Shallow copy is like
        assignment operator.
        ''')
import copy
original_mem = [[1,2,3],[4,5,6],[7,8,'a']]
print(original_mem)
print('Id of original_mem',id(original_mem))
print('Id of 1st element', id(original_mem[0]))
print('Id of 2nd element', id(original_mem[1]))
print('Id of 3rd element', id(original_mem[2]))

new_mem = copy.copy(original_mem)
print('\n',new_mem)
print('Id of new_mem',id(new_mem))
print('Id of 1st element of new_mem',id(new_mem[0]))
print('Id of 2nd element of new_mem',id(new_mem[1]))
print('Id of 1st element of new_mem',id(new_mem[2]))
