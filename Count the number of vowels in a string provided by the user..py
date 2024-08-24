

# Count the number of vowels in a string provided by the user.
string = input("Enter a string: ")
Vowels= 'aeiouAEIOU'
count = 0
for character in string:
    if character in Vowels:
        count = count + 1
print(f"The number of vowels in the string is: {count}")
