#Problem 14: Write a program that recognizes valid hex color value using Regular Expression.
import re

exp = "^([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])$"
result1 = bool(re.match(exp, "192.168.1.1"))
result2 = bool(re.match(exp, "1.1.1.1.1"))

print(result1)
print(result2)