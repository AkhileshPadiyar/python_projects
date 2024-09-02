import random

options = ["rock" , "paper" , "scissors"]

user_wins = 0
computer_wins = 0

while True:
  user_choice = input("Type rock/paper/scissors and Q to quit: ").lower()
  if user_choice == "q":
    break
  if user_choice not in options:
    continue

  random_number = random.randint(0,2)
  computer_choice = options[random_number]
  print("Computer choice was ",computer_choice + "..")

  if user_choice == "rock" and computer_choice == "scissors":
    print("You won!")
    user_wins += 1
  elif user_choice == "paper" and computer_choice == "rock":
    print("You won!")
    user_wins += 1
  elif user_choice == "scissors" and computer_choice == "paper":
    print("You won!")
    user_wins += 1
  else:
    print("Computer won!")
    computer_wins += 1

print("You won",user_wins,"times")
print("Computer won",computer_wins,"times")
print("Goodbye :)")
