from random import randint

NUM1 = randint(1, 50)
NUM2 = randint(1,50)

print("The two numbers are", NUM1, NUM2)

if NUM1 > NUM2:
  Greater = NUM1

else:
  Greater = NUM2

while(True):
  if ((Greater % NUM1 == 0 ) and (Greater % NUM2 == 0)):
    lcm = Greater
    break
  Greater += 1



print("The Lcm of", NUM1, "and", NUM2, "is = ", Greater)

 