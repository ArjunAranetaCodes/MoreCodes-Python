#Problem 19: Write a program that counts the total number
#of vowels in a string.
word = "program"
vowels = "aeiou"
vowelCount = 0

for x in range(0,len(word)):
 if vowels.find(word[x]) != -1:
  vowelCount = vowelCount + 1

print("Total: ", vowelCount)
