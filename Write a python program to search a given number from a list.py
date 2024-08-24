


# Write a python program to search a given number from a list
lis = [10,20,30,40]
search_number =10
found = False
for index in range(len(lis)):
    if lis[index] == search_number:
        print(f"The search number is: {index}")
        found = True
        break
if not found:
        print("Number not found in the lis")    
