
lstNumber = [4, 3, 2, 1]
closest = 0
numDiff = lstNumber[0]

for num in lstNumber:
 diff = 0 - num
 diff = abs(diff)
 if diff < numDiff:
  numDiff = diff
  closest = num

print ("Closest to 0 is ", closest)


