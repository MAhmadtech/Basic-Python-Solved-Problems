


# Write a program that take a user inputr of three angles and will find out whether it can form a triangle or not.
angle1 = int(input("Enter your first angle number: "))
angle2 = int(input("Enter your second angle number: "))
angle3 = int(input("Enter your third angle number: "))
if angle1>0 and angle2 > 0 and angle3 > 0 and (angle1+angle2+angle3)==180:
    print("Yes, these angles can make a triangle")
else:
    print("No, these angles can not make a triengle")     