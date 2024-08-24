

# Write a menu driven program - 1.cm to ft  2.kl to miles  3.usd to inr  4.exit

while True:
    print("Menu:")
    print("1. cm to ft")
    print("2. km to miles")
    print("3. USD to INR")
    print("4. Exit")
    choice = input("Enter your choice (1 to 4): ")
    if choice == '1':  
        cm = float(input("Enter the length in centimeters: "))
        feet = cm * 0.0328084
        print(f"{cm} cm is equal to {feet} feet.")
    elif choice == '2':
        km = float(input("Enter the distance in kilometers: "))
        miles = km * 0.621371
        print(f"{km} km is equal to {miles} miles.")
    elif choice == '3':
        usd = float(input("Enter the amount in USD: "))
        inr = usd * 83
        print(f"{usd} USD is equal to {inr} INR.")
    elif choice == '4':  
        print("Exiting the program.")
        break    
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")


