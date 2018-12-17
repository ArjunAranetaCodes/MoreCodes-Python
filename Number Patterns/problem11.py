"""
Problem 11: Write a program to print the pattern of asterisks using loop.
*
**
***
****
*****
"""
import sys
rows = 6
for y in range(0,rows):
 for x in range(0,y):
  sys.stdout.write('*')
  sys.stdout.flush()
 print()
