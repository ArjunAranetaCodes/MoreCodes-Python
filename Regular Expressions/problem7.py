#Problem 7: Write a program that counts vowels in a String using Regular Expression.
import re

exp = "[^aeiouAEIOU]"
result1 = len(re.sub(exp, "", "Hello World"))

print(result1)