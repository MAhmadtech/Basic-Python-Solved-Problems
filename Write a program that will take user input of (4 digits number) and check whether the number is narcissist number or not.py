

# Write a program that will take user input of (4 digits number) and check whether the number is narcissist number or not
number = int(input("Enter your 4-digit number: "))
num_str = str(number)
if len(num_str)==4:
    total = sum(int(digit)**4 for digit in num_str)
    if total == number:
        print("Yes its a narcissit number")
    else:
        print("No its not a narcissist number")
else:
    print("Please enter the 4-digit number")            

