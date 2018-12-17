"""
Problem 15: Write a program to print the number pattern using loop.
11111
2222
333
44
5
"""
import sys
rows = 5
num = 1
for y in range(rows, 0, -1):
 for x in range(0,y):
  sys.stdout.write(str(num))
  sys.stdout.flush()
 print()
 num = num + 1
