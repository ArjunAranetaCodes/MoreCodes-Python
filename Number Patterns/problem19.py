"""
Problem 19: Write a program to print the number pattern using loop.
11 11
11 11
   
11 11
11 11
"""
import sys, math
row = 5
col = 5
for y in range(0, row):
 for x in range(0, col): 
  if(math.floor(col / 2) == x or math.floor(row / 2) == y) :
   sys.stdout.write(" ")
  elif((col % 2 == 0 and math.floor(col / 2) == x) or (row % 2 == 0 and math.floor(row / 2) == y)) :
   sys.stdout.write(" ")
  else:
   sys.stdout.write("1")
  sys.stdout.flush()
 print()