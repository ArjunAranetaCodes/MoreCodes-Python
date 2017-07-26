#Problem 18: Write a program that outputs the frequency of a
#letter in a string.
word = "program"
letter = "a"
letterCount = 0

for x in range(0,len(word)):
 if letter.find(word[x]) != -1:
  letterCount = letterCount + 1

print("Total: ", letterCount)
