

# Write a python program to remove all the duplicates from a list
# Input list from the user (or assume a given list)
lis = [1,1,2,2,2,3,3,3,4,4,5,5,6,7,7,8]
# user_list = [1, 2, 2, 3, 4, 4, 5]
new_list = []
for element in lis:
    if element not in new_list:
        new_list.append(element)
print(f"The list after removing duplicates: {new_list}")
