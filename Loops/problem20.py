#Problem 20: (RecursioN) Write a program that outputs the
#sum of numbers from 1 to n.
def GetSum(num, sum):
 if num == 0:
  return sum
 else:
  return GetSum((num - 1), (sum + num))

print("Sum is " + str(GetSum(10, 0)))
