#Problem 1: Write a program to test if the first character of the String is uppercase.
import re

exp = "^[A-Z][a-z0-9_-]{3,19}$"
result1 = bool(re.match(exp, "Hello"))
result2 = bool(re.match(exp, "world"))

print(result1)
print(result2)