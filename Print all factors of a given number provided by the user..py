


# Print all factors of a given number provided by the user.

number = int(input("Enter a number: "))
print(f"The factors of a {number} are :")
for i in range(1,number+1):
    if number % i == 0:
        print(i)