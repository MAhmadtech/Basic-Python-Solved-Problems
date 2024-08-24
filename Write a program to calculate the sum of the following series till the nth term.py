



# Write a program to calculate the sum of the following series till the nth term
# 1/1! + 2/2! + 3/3! + 4/4! +…….+ n/n!
# n will be provided by the user

n = int(input("Enter the value of n: "))
total_sum = 0
for i in range(1,n + 1):
    factorial = 1
    for j in range(1,i + 1):
        factorial = factorial * j
    term = i/factorial
    total_sum = total_sum + term
print(f"The sum of the series till the {n} term is {total_sum}")        