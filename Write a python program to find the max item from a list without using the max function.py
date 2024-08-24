

# Write a python program to find the max item from a list without using the max function
# Define the list (or input from the user)
lis =[5, 4 , 6 , 3]
max_value = lis[0]
for item in lis:
    if item > max_value:
        max_value = item 
print(f"The maximum item in the list is: {max_value}")