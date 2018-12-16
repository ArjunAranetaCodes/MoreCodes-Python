"""
Problem 5: Write a program to print the number pattern of ones and zeros using loop.
11111
00000
00000
00000
11111
"""
import sys
for y in range(0,5):
 for x in range(0,5):
  if ((y == 0) or (y == 4)) :
   sys.stdout.write("1")
  else:
   sys.stdout.write("0")
  sys.stdout.flush()
 print()