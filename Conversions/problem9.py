#Problem 9: Write a program that converys a hexadecimal number to decimal number.
import math

dec = 0
hex = "100"

temp = list(hex)
temp.reverse()

for x in range(0, len(hex)):
 dec = dec + (int(temp[x]) * int(math.pow(16, x)))

print(dec)
