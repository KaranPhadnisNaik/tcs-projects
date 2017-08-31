import random

computerGuess = str(random.randint(1,10))
ourGuess = input("Guess a number from 1 to 10: ")
# print ourGuess

isMyGuessWrong = True

while isMyGuessWrong:
  ourGuess = input("Guess a number from 1 to 10: ")
  if ourGuess == computerGuess:
    print "Good job!"
  else:
    print "Try again! The correct computer generated value was "+computerGuess
