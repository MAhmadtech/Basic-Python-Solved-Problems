


# Assume a list with numbers from 1 to 10 and then convert it into a 
# dictionary where the key would be the numbers of the list and the values
# would be the square of those numbers.

lis = [1,2,3,4,5,6,7,8,9,10]
square_dic = {}
for lis in lis:
    square = lis **2
    square_dic[lis] = square
print(square_dic)    