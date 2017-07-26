#Problem 4: Write a program that outputs an asterisk
#pyramid.
import sys
for y in range(1,7):
 for x in range(1,y):
  sys.stdout.write('*')
  sys.stdout.flush()
 print()
