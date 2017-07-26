#Problem 16: Write a program that outputs the factorial
#of a number.
num = 5
fact = 1

for x in range(num, 1, -1):
 fact = fact * x

print("Factorial of 5 is " + str(fact))
