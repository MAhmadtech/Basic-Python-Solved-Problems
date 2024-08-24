


# Write a program that can sort a given unsorted list. Dont use any built in function for sorting.
# Step 1: Define the unsorted list
unsorted_list = [5, 2, 9, 1, 4,3,4,9, 6]
n = len(unsorted_list)
for i in range(n):
    for j in range(0, n-i-1):
        if unsorted_list[j] > unsorted_list[j+1]:
            unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
print("Sorted List:", unsorted_list)
