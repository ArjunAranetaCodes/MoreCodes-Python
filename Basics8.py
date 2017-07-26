#Switch Statement

def switch(argument):
 switcher = {
  1: "Seems it is number 1",
  5: "Feels like it is five or 10",
  10: "Feels like it is five or 10",
 }
 return switcher.get(argument, "0")

print(switch(5))
