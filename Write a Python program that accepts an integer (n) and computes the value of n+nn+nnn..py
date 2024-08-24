

# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

n = (input("Enter an integer: "))

nn = n + n
nnn = n + n + n
result = int(n) + int(nn) + int(nnn)
print(f"The result of {n} + {nn} + {nnn} is : {result}")
