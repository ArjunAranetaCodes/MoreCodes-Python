#Problem 4:Write a program that accepts radius of a circle and
#find its diameter, circumference, and area.
radius = input("Enter value of radius: ")
pi = 3.14
dia = float(radius) * float(radius)
area = pi * dia
cir = 2.0 * pi * float(radius)
print
print("Diameter of the circle is " + str(dia))
print("Area of the circle is " + str(area))
print("Circumference of the circle is " + str(cir))
