


# Write a program that can check whether a given string is palindrome or not.

string = input("Enter a string: ")
reversed_string = string[::-1]
if string == reversed_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
