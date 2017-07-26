 #Problem 8: Write a program that counts vowels in a string.
word = "program"
vowels = "aeiou"
vowelCount = 0

for x in range(0,len(word)):
 if vowels.find(word[x]) != -1:
  vowelCount = vowelCount + 1

print("Total: ", vowelCount)
