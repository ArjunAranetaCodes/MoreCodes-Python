#Problem 15: Write a program that takes a value inside a <div> tag using Regular Expression.
import re

exp = "<(\"[^\"]*\"|\'[^\']*\'|[^\'\">])*>"
result1 = re.sub(exp, "", "<div>Hello World</div>")

print(result1)