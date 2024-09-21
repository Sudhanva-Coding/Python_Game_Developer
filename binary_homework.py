import random

ger = random.randint(0, 100)
print("the number to be converted to its binary form is", ger)

def binary_conversion(x):
  if x > 1:
    binary_conversion(x//2)

  print(x % 2, end = "")

binary_conversion(ger)
print()


#