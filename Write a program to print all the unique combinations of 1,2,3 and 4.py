

# Write a program to print all the unique combinations of 1,2,3 and 4

numbers = [1,2,3,4]
for i in numbers:
    for j in numbers:
        for k in numbers:
            for l in numbers:
                if i!=j and i!=k and i!=l and j!=k and j!=l and k!=l:
                    print(i,j,k,l)