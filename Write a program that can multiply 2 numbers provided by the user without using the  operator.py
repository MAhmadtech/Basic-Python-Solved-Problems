


# Write a program that can multiply 2 numbers provided by the user without using the * operator
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
result = 0
for _ in range (abs(b)):
    result = result + a
if b < 0:
    result = -result
print(f"The product of {a} and {b} is {result}.")    

