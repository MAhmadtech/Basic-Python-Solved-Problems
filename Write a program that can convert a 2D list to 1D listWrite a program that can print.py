

# Write a program that can convert a 2D list to 1D listWrite a program that can print
two_d_list = [ [1,2,3] , [4,5,6] , [7,8,9]]
one_d_lis = []
for sublis in two_d_list:
    for item in sublis:
        one_d_lis.append(item)
print(one_d_lis)        