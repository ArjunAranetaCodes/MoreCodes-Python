#Problem 16: Write a program that takes a value inside a <a> tag using Regular Expression.
import re

exp = "<(\"[^\"]*\"|\'[^\']*\'|[^\'\">])*>"
result1 = re.sub(exp, "", "<a>Hello World</a>")

print(result1)