import random

print("Do you want to play: ");
choice = input();
if choice.lower() != "yes":
  print("Game ended")
  exit()

else :
  print("A random number between 1 - 10 is generated, and you have to guess it")
  print("Let's play :)")

random_number = random.randint(1,10)
guess = 1

while True:
  a = input("Enter a number: ")
  if a.isdigit():
    a = int(a)
    if a > 10 or a < 1:
      print("Enter a number in range 0 - 10")
      continue
  else :
    print("Enter a numerical value")
    continue
  
  if a == random_number:
    print("You found the number!!!!! ")
    print("It took you",guess,"guesses to find the number ",random_number)
    exit()
  elif a > random_number:
    print("Try a lower number")
    guess += 1
  else :
    print("Try a higher number")
    guess += 1