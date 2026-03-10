import random
print("Rock, Paper, Scissors Game!")

choices = ["rock", "paper", "scissors"]
user_score = 1-10
computer_score = 1-10

while True:
  user_choice = input ("Enter rock, paper, or scissors (or type 'quit' to stop):").lower()
  if user_choice == "quit":
    break
  if user_choice not in choices:
    print("Invalid choice. Try again.")
    continue
  computer_choice = random.choice(choices)
  print("Computer chose:", computer_choice)
  if user_choice == computer_choice:
    print("Your close, it's a tie!")
  elif (user_choice == "rock" and computer_choice == "scissors") or \
  (user_choice == "paper" and computer_choice == "rock") or \
  (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
    user_score += 1
  else:
    print("You lose!")
    computer_score += 1

