"""
Problem 17: Write a program to print the number pattern using loop.
1
12
123
1234
12345
1234
123
12
1
"""
import sys
rows = 6
for y in range(0,rows):
 for x in range(1,y):
  sys.stdout.write(str(x))
  sys.stdout.flush()
 print()
for y in range(rows,0,-1):
 for x in range(1,y):
  sys.stdout.write(str(x))
  sys.stdout.flush()
 print()
