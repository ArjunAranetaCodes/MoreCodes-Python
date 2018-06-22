#Problem 8: Write a program that checks if the String if valid url using Regular Expression.
import re

exp = "^(https?:\\/\\/)?(www\\.)?([\\w]+\\.)+[‌​\\w]{2,63}\\/?$"
result1 = bool(re.match(exp, "http://www.example.com"))
result2 = bool(re.match(exp, "wwwexamplecom"))

print(result1)
print(result2)