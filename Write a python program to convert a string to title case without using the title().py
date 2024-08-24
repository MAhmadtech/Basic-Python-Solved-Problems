


# Write a python program to convert a string to title case without using the title()
string = input("Enter a string: ")
words = string.split()
title_words = []
for word in words:
    title_word = word[0].upper() + word[1:].lower()
    title_words.append(title_word)
    title_string = " ".join(title_words)
print(f"The title string is: {title_string}")    