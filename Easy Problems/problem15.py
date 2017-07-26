#Problem 15: Write a program that finds if a string is
#within a string.
word1 = "programming"
word2 = "program"

if word1.find(word2) != -1:
 print(word2, "found")
else:
 print(word2, "not found")
