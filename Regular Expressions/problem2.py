#Problem 2: Write a program that matches email address.
import re

exp = "^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$"
result1 = bool(re.match(exp, "mark@yahoo.com"))
result2 = bool(re.match(exp, "mark-yahoo.com"))

print(result1)
print(result2)