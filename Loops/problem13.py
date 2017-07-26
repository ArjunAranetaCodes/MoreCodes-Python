 #Problem 13: Write a program that reverses a string.
word = "MoreCodes"
newWord = ""

for x in range(len(word) - 1, -1, -1):
 newWord = newWord + str(word[x])

print(newWord)
