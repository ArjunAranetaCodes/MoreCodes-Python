#Problem 11: Write a program that counts the occurrence of a string in a string using Regular Expression.
import re

exp = "Hello"
word = "HelloWorldHelloWorld"
newword = re.sub(exp, "", word)
count = (len(word) - len(newword)) / len(exp)

print(count)