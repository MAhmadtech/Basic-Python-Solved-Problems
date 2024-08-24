


# Write a Python Program to Find the Sum of the Series till the nth term: 
# 1 + x^2/2 + x^3/3 + … x^n/n
# n will be provided by the user

x = float(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))

series_sum = 1


for i in range(2, n + 1):
    term = (x ** i) / i  
    series_sum = series_sum +  term
print(f"The sum of the series is : {series_sum}")

