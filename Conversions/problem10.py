#Problem 10: Write a program that converts a decimal number to octal number.
dec = 256
oct = ""

while dec > 0:
 oct = str(dec % 8) + oct
 dec = int(dec / 8)

print(oct)
