#Problem 19: Write a program that converts numbers to words.
def NumberToWords(number, word):
 if (number >= 1) and (number <= 19):
  map = ["One", "Two", "Three", "Four", "Five", "Six", "Seven",
    "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
    "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
  word = map[int(number - 1)]
  return word
 elif (number >= 20) and (number <= 99):
  map = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy",
    "Eighty", "Ninety"]
  word = map[int((number - 1) - 3)];
  return word + " " + NumberToWords(number % 10, "")
 elif (number >= 100) and (number <= 999):
  return (NumberToWords(number / 100, "") + " Hundred " +
  NumberToWords(number % 100, ""))
 elif (number >= 1000) and (number <= 9999):
  return (NumberToWords(number / 1000, "") + " Thousand " +
  NumberToWords(number % 1000, ""))
 elif (number >= 1000000) and (number <= 999999999):
  return (NumberToWords(number / 1000000, "") + " Million " +
  NumberToWords(number % 1000000, ""))
 return word

print(NumberToWords(1000, ""))
