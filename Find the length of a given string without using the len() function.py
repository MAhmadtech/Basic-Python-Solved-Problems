

# Find the length of a given string without using the len() function
string = input("Enter a string: ")
length = 0
for character in string:
    length = length + 1
print(f"The length of strings character are: {length}")