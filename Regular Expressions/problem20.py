#Problem 20: Write a program that validates if string length is between 5 to 10 using Regular Expression.
import re

exp = "\\w{5,10}\\b"
result1 = bool(re.match(exp, "Hello"))
result2 = bool(re.match(exp, "Hi"))

print(result1)
print(result2)