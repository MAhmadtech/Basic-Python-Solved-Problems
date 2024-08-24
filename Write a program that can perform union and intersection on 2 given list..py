

# Write a program that can perform union and intersection on 2 given list.

lis1 = [1,2,3,4]
lis2 = [3,4,5,6]
union_lis = []
intersection_lis = []
for item in lis1:
    if item not in union_lis:
        union_lis.append(item)
for item in lis2:
    if item not in union_lis:
        union_lis.append(item)              
for item in lis1:
    if item in lis2 and item not in intersection_lis:
        intersection_lis.append(item)
print(f"The union lis is: {union_lis}")
print(f"The initersection lis is: {intersection_lis}")        

     
