"""
Problem 12: Write a program to print the pattern of asterisks using loop.
*****
****
***
**
*
"""
import sys
rows = 5
for y in range(rows,0,-1):
 for x in range(0,y):
  sys.stdout.write('*')
  sys.stdout.flush()
 print()
