#Problem 10: Write a program to check whether a given
#number is an armstrong number or not.
num = 371
sum = 0
temp = 0
rmdr = 0

temp = num

while (temp != 0):
 rmdr = int(temp % 10)
 sum = sum + (rmdr * rmdr * rmdr)
 temp = int(temp / 10)

if num == sum:
 print("Armstrong number")
else:
 print("Not an Armstrong number")
