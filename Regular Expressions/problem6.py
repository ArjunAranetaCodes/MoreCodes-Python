#Problem 6: Write a program that removes white space and non-visible characters.
import re

exp = "\\s"
result1 = re.sub(exp, "", "Hello World")

print(result1)