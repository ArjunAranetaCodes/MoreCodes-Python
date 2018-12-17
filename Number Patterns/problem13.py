"""
Problem 13: Write a program to print the pattern of asterisks using loop.
*
**
***
****
*****
****
***
**
*
"""
import sys
rows = 5
for y in range(0,rows):
 for x in range(0,y):
  sys.stdout.write('*')
  sys.stdout.flush()
 print()
 
for y in range(rows,0,-1):
 for x in range(0,y):
  sys.stdout.write('*')
  sys.stdout.flush()
 print()
