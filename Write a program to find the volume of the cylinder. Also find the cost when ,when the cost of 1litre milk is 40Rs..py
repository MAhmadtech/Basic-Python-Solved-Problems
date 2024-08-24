

# Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.

radius = int(input("Enter your radius: "))
height = int(input("Enter your height: "))
cost_per_litre = 40

volume = 3.14159 * radius**2 * 100
volume_in_litre = volume * 0.001
total_cost = volume_in_litre * cost_per_litre
print("Your total cost is: ", total_cost)