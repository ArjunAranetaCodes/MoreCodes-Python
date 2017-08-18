
arrNumber = [4, 3, 2, 1]
closest = 0
numDiff = arrNumber[0]

for num in arrNumber:
 diff = 0 - num
 diff = abs(diff)
 if diff < numDiff:
  numDiff = diff
  closest = num

print ("Closest to 0 is ", closest)


