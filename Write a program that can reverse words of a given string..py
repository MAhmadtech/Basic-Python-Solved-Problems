


# Write a program that can reverse words of a given string.
# Eg if the input is Hello how are you
# Output should be you are how Hello


string = "Hello how are you"
word = string.split()
reversed_word = word[::-1]
reversed_string = ' '.join(reversed_word)
print(f"The reversed string is: {reversed_string}")


