'''
# filter() function Problems
# Write a program to filter vowels from the sentence
'''
vowels_list = ['a','e','i','o','u']
string_input = input("Enter your sentence:")

def filter_vowels(ch):
    if ch in vowels_list:
        return True
        
output = list(filter(filter_vowels,string_input))
print(output)

#Write same logic using lambda function
lambo_out=lambda ch: ch in vowels_list
output_lambo = list(filter(lambo_out,string_input))
print("This is lambo: ",output_lambo)

#Ex_2 filter students having marks greater than or equal to 90
data = {'Nitesh':78,'Rahul':98,'Raj':91,'Amar':90,'Abhi':81}

def toppers(student):
    return data[student]>=90

print("Toppers:",list(filter(toppers,data)))