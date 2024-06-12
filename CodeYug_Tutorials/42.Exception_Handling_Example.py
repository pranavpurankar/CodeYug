'''
Question:
    Write a program that will sum numbers present in given list of data.
    
    excepted output:- 
    enter the list:- [1,'a','b',3]
    item 'a' is not a number
    item 'b' is not a number
    Total is : 4
'''


def sum_of_int_list(my_list):
    total = 0
    for ele in my_list:
        try:
            int(ele)
        except Exception:
            print(f"item {ele} is not a number")
        else:
            total = total + ele
    return total


print(sum_of_int_list([1, 'a', 'b', 3, 'ab', 10]))   # [1,'a','b',3]
