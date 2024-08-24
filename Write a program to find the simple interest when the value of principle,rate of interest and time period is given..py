


# Write a program to find the simple interest when the value of principle,rate of interest and time period is given.


principle = int(input("Enter your invest amount or borrow amount: "))
Rate_of_Interest = int(input("Enter your rate of interst: "))
time_period =int(input("Enter your time period: "))
simple_interest = principle * Rate_of_Interest * time_period / 100
print("your simple interest are :", simple_interest)