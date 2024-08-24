

# Write a program that can create a new list from a given list where each item in the new list is square of the item of the old list
original_list = [1, 2, 3, 4, 5]
squared_list = []
for item in original_list:
    square = item ** 2
    squared_list.append(square)
print(f"The squared list is: {squared_list}")
