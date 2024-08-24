

# Write a program to check if a list is in ascending order or not

# Define the list (or input from the user)
lis = [1, 2, 3, 4, 5]
ascending = True
for i in range(len(lis) - 1):
    if lis[i] > lis[i + 1]:
        ascending = False
        break
if ascending:
    print("List is in ascending order.")
else:
    print("List is not in ascending order.")
