#Problem 9: Write a program that accepts a number
#and outputs 1 to the input (1 to n).
num = input("Enter value of num: ")
sum = 0
for x in range(1,int(num) + 1):
 sum = sum + x

print ("The sum of 1 to " + str(num) + " is " + str(sum))
