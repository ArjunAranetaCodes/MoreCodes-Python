#Problem 3: Write a program that checks if string contains sample format date of (yyyy-mm-dd)
import re

exp = "([0-9]{4})-([0-9]{2})-([0-9]{2})"
result1 = bool(re.match(exp, "2018-01-02"))
result2 = bool(re.match(exp, "01-01-02"))

print(result1)
print(result2)