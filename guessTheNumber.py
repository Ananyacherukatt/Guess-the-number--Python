from random import randint


EASY_LEVEL=10
HARD_LEVEL=5


# function to check user's guess against actual number
def check(guess,answer,turns):
  if guess>answer:
    print("Too high")
    return turns-1
  elif guess<answer:
    print("Too low")
    return turns-1
  else:
    print(f"You got it!!: The answer is {answer}")
# make function to set difficulty
def set_difficulty():
  level=input("Choose the difficulty 'easy' or 'hard': ")
  if level=="easy":
    return EASY_LEVEL
  else:
    return HARD_LEVEL
def game():
# choosing a random number between 1 and 100
  print("Welcome to the number guessing game!!!")
  print("I'm thinking a number between 1 and 100")
  answer=randint(1,100)
  print(f"the correct answer is {answer}")
  turns=set_difficulty()
  
  # let the user guess a number
  guess=0
  while guess!=answer:
    print(f"you have {turns} no.of chances remaining")
    
    guess=int(input("Make a guess: "))
    turns= check(guess,answer,turns)
    if turns==0:
      print("you ran out of chances!!! you lose")
      return
    elif guess!=answer:
      print("guess again")

game()