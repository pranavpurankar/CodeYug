'''
Excception handling in input functions
'''


def get_square():
    try:
        num = int(input("Enter the number: "))  # Hello
        print("Square is: ", num**2)
    except Exception as e:
        print(e)
        get_square()


get_square()

print("rest of code\n")


# A pitfall in exception handling


try:
    f = open('leetcode1.txt', mode = 'r')
    my_data = f.read()
    print(my_data)

except Exception as err:
    print(err)

else:
    print("Read operation success")

finally:
    try:
        f.close()
    except:
        pass
    print("Rest of code")
