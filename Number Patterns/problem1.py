"""
Problem 1: Write a program to print the number pattern of ones and zeros using loop.
11111
11111
11111
11111
11111
"""
import sys
for y in range(1,7):
 for x in range(1,y):
  sys.stdout.write('*')
  sys.stdout.flush()
 print()