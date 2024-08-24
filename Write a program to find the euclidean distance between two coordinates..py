
import math
# Write a program to find the euclidean distance between two coordinates.

x1, y1 = map(float, input("Enter coordinates of the first point (x1 y1): ").split())
x2, y2 = map(float, input("Enter coordinates of the second point (x2 y2): ").split())
dx = x2 - x1
dy = y2 - y1

distance = math.sqrt(dx**2 + dy**2)


print("The Euclidean distance between the points is:",distance)
