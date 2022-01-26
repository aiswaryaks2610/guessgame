import random

i="yes"
while(i=="yes"):
  q=int(input("guess a number between 0 to 10 "))
  r=random.randint(0,10)
  if q==r:
    print("you are right")
  else:
    print("soryyy :(")
    print(f"the number computer kept in secret was {r} ")
  print("do you wanna play again ")
  e=input()
  if e=="yes":
    i="yes"
  else:
    i="no"
    quit()
