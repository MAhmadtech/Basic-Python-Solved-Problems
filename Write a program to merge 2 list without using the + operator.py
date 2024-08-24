


# Write a program to merge 2 list without using the + operator

list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = []
for item in list1:
    merged_list.append(item)
for item in list2:
    merged_list.append(item)
print(f"The merged list is: {merged_list}")
