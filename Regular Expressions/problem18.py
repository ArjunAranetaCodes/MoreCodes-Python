#Problem 18: Write a program that extracts string inside quotation marks using Regular Expression.
import re

exp = "\'([^\"]*)\'"
result1 = re.search(exp, "Hello 'World'")

print(result1.group())