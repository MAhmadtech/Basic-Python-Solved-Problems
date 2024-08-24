



# Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

number = int(input("Enter a four-digit number: "))
thousands = number // 1000             
hundreds = (number % 1000) // 100      
tens = (number % 100) // 10            
ones = number % 10                     
reversed_number = ones * 1000 + tens * 100 + hundreds * 10 + thousands
if number == reversed_number:
    print("Yes, reverse is true.")
else:
    print("No, reverse is not true.")