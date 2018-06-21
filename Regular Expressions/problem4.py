#Problem 4: Write a program that matches time in 12 hour format.
import re

exp = "(((0[1-9])|(1[0-2])):([0-5])([0-9])\\s(a|p)m)"
result1 = bool(re.match(exp, "08:01 am"))
result2 = bool(re.match(exp, "18:01 pm"))

print(result1)
print(result2)