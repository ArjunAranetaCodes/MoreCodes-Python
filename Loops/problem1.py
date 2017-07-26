#Problem 1: Write a program that prints the numbers from 1 to 50.
#Output "Fizz" for multiples of 3, output "Buzz" for multiples of 5, and
#both "FizzBuzz" for multiples of both 3 and 5.
for x in range(1,51):
 if x % 3 == 0 and x % 5 == 0:
  print("FizzBuzz")
 elif x % 3 == 0:
  print("Fizz")
 elif x % 5 == 0:
  print("Buzz")
 else:
  print(x)
