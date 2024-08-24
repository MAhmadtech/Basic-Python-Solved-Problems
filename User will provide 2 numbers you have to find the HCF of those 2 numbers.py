



# User will provide 2 numbers you have to find the HCF of those 2 numbers
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
while num2 !=0:
    num1,num2 = num2 , num1 % num2
    print(f"The HCF is {num1}")