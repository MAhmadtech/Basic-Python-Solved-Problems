


# Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the numbers.

total_sum = 0
count = 0
while True:
    n = int(input("Enter a number and (0 to stop): "))
    if n == 0:
        break
    total_sum = total_sum + n
    count = count + 1
if count > 0:
    average = total_sum/count
    print(f" The sum of all numbers is: {total_sum}")
    print(f"The average of all numbers is: {average}")
else:
    print("No number were entered")        
