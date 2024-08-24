



# Write a program to find the compound interest
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time period (in years): "))
n = int(input("Enter the number of times interest is compounded per year: "))
rate = rate / 100
amount = principal * (1 + rate / n) ** (n * time)
compound_interest = amount - principal
print(compound_interest)
