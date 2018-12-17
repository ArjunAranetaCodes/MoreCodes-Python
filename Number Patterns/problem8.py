"""
Problem 8: Write a program to print the number pattern of ones and zeros using loop.
11111
11111
11011
11111
11111
"""
import sys, math
row = 5
col = 5
for y in range(0,5):
 for x in range(0,5):
  if(x == math.floor(row / 2) and y == math.floor(col / 2)) :
   sys.stdout.write("0")
  else:
   sys.stdout.write("1")
  sys.stdout.flush()
 print()