



# Count the frequency of a particular character in a provided string. Eg 'hello how are you' is the string, the frequency of h in this string is 2.
string = input("Enter a string: ")
char_t0_character = input("Enter a character to count: ")
count = 0
for character in string:
    if character == char_t0_character:
        count = count + 1
print(f"The frequency of {char_t0_character}in the string is: {count}")    