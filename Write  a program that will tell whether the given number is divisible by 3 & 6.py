

# Write  a program that will tell whether the given number is divisible by 3 & 6

number = int(input("Enter your number: "))

if number%3 == 0 and number % 6 ==0:
    print("Yes both number 3 and 6 are divisible")
else:
    print("No both number 3 and 6 are not divisible")

