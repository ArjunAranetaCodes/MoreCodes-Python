#Problem 7: Write a program that converts a decimal number to binary number.
dec = 10
binary = ""

while dec > 0:
 binary = str(dec % 2) + binary
 dec = int(dec / 2)

print(binary)
