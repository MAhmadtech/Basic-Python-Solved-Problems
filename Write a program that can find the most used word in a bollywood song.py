


# Write a program that can find the most used word in a bollywood song
lyrics = "la la la la , lala la la la"
lyrics = lyrics.lower()
words = lyrics.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
most_used_word = max(word_count, key=word_count.get)
most_used_word_count = word_count[most_used_word]
print("Most used word:", most_used_word)
print("Frequency:", most_used_word_count)
