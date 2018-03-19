#Problem 8: Write a program that converts a decimal number to hexadecimal number.
dec = 256
hex = ""

while dec > 0:
 hex = str(dec % 16) + hex
 dec = int(dec / 16)

print(hex)
