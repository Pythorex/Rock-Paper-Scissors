import random

print("Hello, welcome to my Rock Paper Scissors Program!")

while True:
  RPS = input("Please enter R for rock, P for paper, or S for scissors. ")

  aichoices = ["rock", "paper", "scissors"]
  aifinalchoice = random.choice(aichoices)

  if RPS == "R":
    if aifinalchoice == "rock":
      print("Computer chose ", aifinalchoice, ". ", "Tie!")
      break
    elif aifinalchoice == "paper":
      print("Computer chose ", aifinalchoice, ". ", "You lose!")
      break
    elif aifinalchoice == "scissors":
      print("Computer chose ", aifinalchoice, ". ", "You win!")
      break
  elif RPS == "P":
    if aifinalchoice == "rock":
      print("Computer chose ", aifinalchoice, ". ", "You win!")
      break
    elif aifinalchoice == "paper":
      print("Computer chose ", aifinalchoice, ". ", "Tie!")
      break
    elif aifinalchoice == "scissors":
      print("Computer chose ", aifinalchoice, ". ", "You lose!")
      break
  elif RPS == "S":
   if aifinalchoice == "rock":
      print("Computer chose ", aifinalchoice, ". ", "You lose!")
      break
   elif aifinalchoice == "paper":
     print("Computer chose ", aifinalchoice, ". ", "You win!")
     break
   elif aifinalchoice == "scissors":
     print("Computer chose ", aifinalchoice, ". ", "Tie!")
     break
  else:
    print("Computer chose ", aifinalchoice, ". ", "Invalid response.")
    break
    
    


