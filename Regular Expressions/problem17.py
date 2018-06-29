#Problem 17: Write a program that removes the last word in a string using Regular Expression.
import re

exp = "\\w+$"
result1 = re.sub(exp, "", "Hello World")

print(result1)