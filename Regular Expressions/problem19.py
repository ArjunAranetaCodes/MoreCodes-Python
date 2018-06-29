#Problem 19: Write a program that counts all numbers in a string using Regular Expression.
import re

exp = "[^0-9]"
result1 = len(re.sub(exp, "", "Hello World123"))

print(result1)