

#Create 2 lists from a given list where 1st list will contain all the odd 
# numbers from the original list and the 2nd one will contain all the even numbers 
lis = [1,2,3,4,5,6,7]

odd_lis = []
even_lis = []
for lis in lis:
    if lis % 2 == 0:
        even_lis.append(lis)
    else:
        odd_lis.append(lis)
print(f"These are even numbers: {even_lis}")
print(f"These are odd numbers: {odd_lis}")            
      