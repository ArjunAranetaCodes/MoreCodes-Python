#Problem 17: Write a program that outputs the index
#of the first occurrence of the letter in a string.
word = "program"
letter = "a"

if word.find(letter) != -1:
 print("Contains a")
else:
 print("Does not contain a")
