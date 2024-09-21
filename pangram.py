# a quick brown fox jumps over the lazy dog

# Pangram : 123 : abc1lk2peg'oidjvhjs3

dsa = input("Please enter a string : ")
ved = "abcdefghijklmnopqrstuvwxyz" 
def pangramcheck (str):
  for i in ved:
    if i not in str.lower():
      return False


  return True


if (pangramcheck(dsa) == True):
  print("yes")

else:
  print("no")
  