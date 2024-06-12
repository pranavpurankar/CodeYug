"""
Types of comprehension
1. list 2. set 3. dictionary

‣ Syntax-01:- Normal
    [expression for variable in iterable]

‣ Syntax-02:- If condition
    [expression for variable in iterable if cond]

‣ Syntax-03:- Nested if's
    [expression for variable in iterable if cond1 if cond2]

‣ Syntax-04:- If-else
    [expression if cond else expression for variable in iterbale]
"""
# Ex_ Syntax-01 [expression for variable in iterable]

nums = [3,6,8,12,14,15]
sq = []
for num in nums:
    sq.append(num*num)
print(sq)

print([num*num for num in nums])

# Ex_ Syntax-02 [expression for variable in iterable if condition]
print("\nFind the squares of even numbers only")
print("\n[Syntax: expression for variable in iterable if cond]")

sq1=[]
for num in nums:
    if num %2==0:
        sq1.append(num*num)
print(sq1)

print([num*num for num in nums if num%2==0])

# Ex_ Syntax-03 [expression for variable in iterable if cond1 if cond2]
print("\nFind out square of num divisible by 3 and 4")
print("Syntax: expression for variable in iterable if cod1 if cond2")

sq3 = []
for num in nums:
    if num%2==0:
        if num%3==0:
            sq3.append(num*num)
print(sq3)

print("Using list compre: ",[num*num for num in nums if num%2==0 if num%3==0])

# Ex_ Syntax-04 [expression if cond else expression for variable in iterable]
print("\nIf I get a even number I will find square of that number if even => cube resp")
print("Syntax: expression if cond else expression for variable in iterable")

result = []
for num in nums:
    if num%2==0:
        result.append(num**2)
    else:
        result.append(num**3)
print(result)

print([num**2 if num%2==0 else num**3 for num in nums])
