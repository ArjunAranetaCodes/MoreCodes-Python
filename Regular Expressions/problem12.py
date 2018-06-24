#Problem 12: Write a program that counts the occurrence of digits in a string using Regular Expression.
import re

exp = "\\D"
result1 = len(re.sub(exp, "", "Hello12 World12"))

print(result1)