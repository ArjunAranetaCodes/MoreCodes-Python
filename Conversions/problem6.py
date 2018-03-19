#Problem 6: Write a program that converts a binary number to decimal number.
import math

dec = 0
binary = "110"

temp = list(binary)
temp.reverse()

for x in range(0, len(binary)):
 dec = dec + (int(temp[x]) * int(math.pow(2, x)))

print(dec)
