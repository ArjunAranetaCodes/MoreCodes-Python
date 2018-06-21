#Problem 5: Write a program that matches time in 24 hour format.
import re

exp = "^(0?[1-9]|1[012])(:[0-5]\d) [APap][mM]$"
result1 = bool(re.match(exp, "13:00"))
result2 = bool(re.match(exp, "8:01 am"))

print(result1)
print(result2)