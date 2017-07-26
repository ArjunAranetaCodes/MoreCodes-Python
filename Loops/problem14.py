#Problem 14: Write a program that accepts 5 numbers
#and outputs the average.
num = 0
sum = 0
ave = 0

for x in range(0, 5):
 num = int(input("Enter a number: "))
 sum = sum + num

ave = sum / 5;
print("Average is " + str(ave))
