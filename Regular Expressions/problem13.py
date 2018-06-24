#Problem 13: Write a program that recognizes valid hex color value using Regular Expression.
import re

exp = "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
result1 = bool(re.match(exp, "#fff"))
result2 = bool(re.match(exp, "#asdf"))

print(result1)
print(result2)