



# Write a program to replace an item with a different item if found in the list
lis = ["Ahmad" , " Ali" , "Abdullah" ]

replace_name = "Abdullah"
new_name = "zain"

for i in range(len(lis)):
    if lis[i] == replace_name:
        lis[i] = new_name
print(lis)        

