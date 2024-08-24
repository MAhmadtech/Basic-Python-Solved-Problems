


# Find the index position of a particular character in another string. 
string = input("Enter a string: ")
char_t0_character = input("Enter a character to index: ")
index = -1
for i in range(len(string)):
    if string[i] == char_t0_character:
        index = i
        break
if index != -1:
    print(f"The index postion of {char_t0_character} is: {index}")
else:
    print(f"The character {char_t0_character} are not found")    
