


# User will provide 2 numbers you have to find the by LCM of those 2 numbers
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
if num1 > num2:
    greater = num1
else:
    greater = num2
while True:
    if greater % num1==0 and greater % num2 ==0:
        lcm = greater 
        break
    greater = greater + 1 
print(f"The LCM of {num1} and {num2} is {lcm}")
