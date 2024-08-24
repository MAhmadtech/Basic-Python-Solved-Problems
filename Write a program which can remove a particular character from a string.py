

# Write a program which can remove a particular character from a string
string = input("Enter a string: ")
char_to_character = input("Enter a character to remove: ")
new_string = ""
for character in string:
    if character != char_to_character:
        new_string = new_string + character
print(f"The new string is : {new_string}")        
