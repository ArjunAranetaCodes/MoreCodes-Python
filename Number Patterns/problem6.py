"""
Problem 6: Write a program to print the number pattern of ones and zeros using loop.
11111
10001
10001
10001
11111
"""
import sys
for y in range(0,5):
 for x in range(0,5):
  if((y == 0) or (y == 4) or (x == 0) or (x == 4)) :
   sys.stdout.write("1")
  else:
   sys.stdout.write("0")
  sys.stdout.flush()
 print()