#Problem 19: (Recursion) Write a program that outputs
#all even numbers below 20.
def PrintEven(num):
 if num == 0:
  return num
 else:
  if num % 2 == 0:
   print(num)
  return PrintEven(num - 1)

PrintEven(10)
