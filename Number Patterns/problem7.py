"""
Problem 7: Write a program to print the number pattern of ones and zeros using loop.
10101
01010
10101
01010
10101
"""
import sys
count = 0
for y in range(0,5):
 for x in range(0,5):
  count += 1
  if(count % 2 == 1) :
   sys.stdout.write("1")
  else:
   sys.stdout.write("0")
  sys.stdout.flush()
 print()