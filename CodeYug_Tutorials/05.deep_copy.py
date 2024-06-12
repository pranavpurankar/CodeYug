print('''
        \n Deep Copy Tutorial
        Deep copy can be done using copy module.
        When we do deep copy it will create a new
        memory allocation. It means when we create
        deep copy and made changes to the newly
        copied object; it won't change the original
        object.
        ''')

import copy

original_mem = [[1,2,3],[4,5,6],[7,8,'a']]
print(original_mem)
print('Id of original_mem',id(original_mem))
print('Id of 1st element', id(original_mem[0]))
print('Id of 2nd element', id(original_mem[1]))
print('Id of 3rd element', id(original_mem[2]))


new_mem = copy.deepcopy(original_mem)
new_mem[2][2]="pranav"
print('\n',new_mem)
print('Id of new_mem',id(new_mem))
print('Id of 1st element of new_mem',id(new_mem[0]))
print('Id of 2nd element of new_mem',id(new_mem[1]))
print('Id of 1st element of new_mem',id(new_mem[2]))
print('No changes made to the original_mem', original_mem)
