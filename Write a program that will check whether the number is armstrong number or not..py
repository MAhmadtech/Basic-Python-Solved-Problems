

# Write a program that will check whether the number is armstrong number or not.

number = int(input("Enter a number: "))
num_str = str(number)
total_digits = len(num_str)
total = sum(int(digit)** total_digits for digit in num_str)
if total == number:
    print("Yes it is a armstrom number")
else:
    print("No its not a armstrom number")    