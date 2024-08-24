

# Write a program that can find the factorial of a given number provided by the user.

n = int(input("Enter a number to find the factorial: "))
factorial = 1
for i in range(1,n+1):
    factorial = factorial * i
print(f"The factorial of {n}! are {factorial}!")    