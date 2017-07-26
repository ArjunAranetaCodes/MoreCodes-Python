#Problem 20: Write a program that checks if a string is a
#palindrome.
word = "anna"
tempWord = ''.join(reversed(word))

if word == tempWord:
 print("Palindrome")
else:
 print("Not Palindrome")
