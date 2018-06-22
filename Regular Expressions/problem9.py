#Problem 9: Write a program that checks if the string is alphanumeric using Regular Expression.
import re

exp = "(([A-Z].*[0-9])|([0-9].*[A-Z]))"
result1 = bool(re.match(exp, "HelloWorld"))
result2 = bool(re.match(exp, "HelloWorld123"))

print(result1)
print(result2)