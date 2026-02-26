import math

print("Enter coordinates for the first point")
x1=float(input("Enter the x1 coordinate: "))
y1=float(input("Enter the y1 coordinate: "))

print("Enter coordinates for the second point")
x2=float(input("Enter the x2 coordinate: "))
y2=float(input("Enter the y2 coordinate: "))

distance=math.sqrt((x2-x1)**2 + (y2-y1)**2)

print("Distance is:",distance)


