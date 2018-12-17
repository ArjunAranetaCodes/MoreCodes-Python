"""
Problem 10: Write a program to print the number pattern using loop.
12345
23456
34567
45678
56789
"""
import sys, math
row = 5
col = 5
min = 1
for y in range(0, row):
 num = min + y
 for x in range(0, col):   
  sys.stdout.write(str(num))
  num = num + 1
  sys.stdout.flush()
 print()