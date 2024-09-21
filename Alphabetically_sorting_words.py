red =  str(input("please enter a string : "))
green = [word.lower() for word in red.split()]
green.sort()

print("the sorted words are : ")
for word in green:
  print(word)


# for x in 