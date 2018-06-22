#Problem 10: Write a program that prints an integer with commas separator using Regular Expression.
import re

exp = "(\\d)(?=(\\d{3})+$)"
result1 = re.sub(exp, "1,", "1000")

print(result1)