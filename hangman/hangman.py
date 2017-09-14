import os
import random

FILE = 'words-corpus.txt'

class Hangman():
    def __init__(self):
        print "Welcome to Hangman!"
        print "(1) Play?\n(2) Exit"
        user_choice_1 = raw_input("->")

        if user_choice_1 == '1':
            print "Starting up game...\n"
            self.start_game()
        elif user_choice_1 == '2':
            print "Goodbye.\n"
            exit()
        else:
            print "Sorry please input either 1 or 2 as an option."
            self.__init__()

    def start_game(self):
        print "========= RULES ========="
        print "A random word will be generated that you need to guess."
        print "Guess one letter at a time."
        print "If you make 6 wrong guesses, you lose!"
        print "=========================\n"
        self.play()
        return

    def get_random_line(self):
        with open(FILE) as f:
            line = random.sample(f.readlines(),1)
            return line[0][:-1]

    def play(self):
        guesses = 0
        used = ""
        final = ""

        word = self.get_random_line()
        progress = ["?" for letter in word]
        # remove EOF character
        progress = progress[1:]
        while guesses < 6:
            if final == word[:-1]:
                print "==============================="
                print "==                           =="
                print "==         YOU WIN!          =="
                print "==                           =="
                print "==============================="
                return
            print ""
            guess = raw_input("Guess a letter -> ").lower()

            if guess in word and guess not in used:
                print "Your guess was RIGHT!"
                used += "," + guess if used!="" else guess
                self.hangman_graphic(guesses,word)
                final = self.update(guess, word, progress)
                print "Progress: " + final
                print "Letter used: " + used

            elif guess not in word and guess not in used:
                if len(guess) > 1 or not guess.isalpha():
                    print "Please enter a single letter! No numbers or punctuation allowed either!"
                    continue

                guesses += 1
                print "Well? That guess was WRONG!"
                used += "," + guess if used!="" else guess
                self.hangman_graphic(guesses, word)
                print "Progress: " + "".join(progress)
                print "Letter used: " + used
            else:
                print "That's the wrong letter!"
                print "Try again!"

    def hangman_graphic(self, guesses, word):
        if guesses == 0:
            print "________      "
            print "|      |      "
            print "|             "
            print "|             "
            print "|             "
            print "|             "
        elif guesses == 1:
            print "________      "
            print "|      |      "
            print "|      O      "
            print "|             "
            print "|             "
            print "|             "
        elif guesses == 2:
            print "________      "
            print "|      |      "
            print "|      O      "
            print "|       \     "
            print "|             "
            print "|             "
        elif guesses == 3:
            print "________      "
            print "|      |      "
            print "|      O      "
            print "|      |\     "
            print "|             "
            print "|             "
        elif guesses == 4:
            print "________      "
            print "|      |      "
            print "|      O      "
            print "|     /|\     "
            print "|             "
            print "|             "
        elif guesses == 5:
            print "________      "
            print "|      |      "
            print "|      O      "
            print "|     /|\     "
            print "|       \     "
            print "|             "
        else:
            print "________      "
            print "|      |      "
            print "|      O      "
            print "|     /|\     "
            print "|     / \     "
            print "|             "
            print "Well it looks like you LOST"
            print "The correct word was "+word.upper()
            print "GAME OVER!"

    def update(self, guess, word, progress):
        i = 0
        for i in range(len(word)):
            if guess == word[i]:
                progress[i] = guess
                i += 1
            else:
                i += 1

        return "".join(progress)

game = Hangman()
