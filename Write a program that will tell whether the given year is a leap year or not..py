



# Write a program that will tell whether the given year is a leap year or not.

year = int(input("Enter the year: "))
if year % 4 == 0:
    print("It might be a leap year")
elif year % 100 == 0:
    print("Its not a  leap year")
elif year % 400 == 0:
    print("It is a leap year")
else:
    print("It not be a leap year")            