"""
Problem 14: Write a program to print the number pattern using loop.
1
22
333
4444
55555
"""
import sys
rows = 6
for y in range(0,rows):
 for x in range(0,y):
  sys.stdout.write(str(y))
  sys.stdout.flush()
 print()
