

# Write a program that accepts 2 numbers from the user a numerator and a denominator and then simplifies it
# Eg if the num = 5, den = 15 the answer should be ⅓
# Eg if the num = 6, den = 9 the answer should be ⅔

numerator = int(input("Enter the Numerator number: "))
denominator = int(input("Enter the denominator number: "))
gcd = 1
for i in range(1,min(numerator,denominator)+ 1):
    if numerator % i == 0 and denominator % i == 0:
        gcd = i
simplified_numerator = numerator//gcd
simplified_denominator = denominator//gcd
print(f" The simplifies fraction is {simplified_numerator}/{simplified_denominator}")        

