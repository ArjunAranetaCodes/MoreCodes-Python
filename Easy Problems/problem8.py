#Problem 8: Write a program that outputs all numbers divisible by
#5 from 1 to 30.
sum = 0
for x in range(1,31):
 if x % 5 == 0:
  sum = sum + x

print("The sum of numbers divisible by 5 from 1 to 30 is " + str(sum))
