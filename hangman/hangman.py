import os
import random

FILE = 'words-corpus.txt'

class Hangman():
    def __init__(self):
        print "Welcome to 'Hangman', are you ready to die?"
        print "(1)Yes, for I am already dead.\n(2)No, get me outta here!"
        user_choice_1 = raw_input("->")

        if user_choice_1 == '1':
            print "Loading nooses, murderers, rapists, thiefs, lunatics..."
            self.start_game()
        elif user_choice_1 == '2':
            print "Bye bye now..."
            exit()
        else:
            print "I'm sorry, I'm hard of hearing, could you repeat that?"
            self.__init__()

    def start_game(self):
        print "Guess the right words and you can live to see another day."
        print "But don't get so happy yet."
        print "If you make 6 wrong guess, YOU'RE TOAST! VAMANOS!"
        self.core_game()
        return

    def get_random_line(self):
        total_bytes = os.stat(FILE).st_size
        random_point = random.randint(0, total_bytes)
        file = open(FILE)
        file.seek(random_point)
        file.readline() # skip this line to clear the partial line
        return file.readline()

    def core_game(self):
        guesses = 0
        letters_used = ""
        the_word = self.get_random_line()
        #print(the_word)
        progress = ["?" for letter in the_word]
        # remove EOF character
        progress = progress[1:]
        final = ""
        while guesses < 6:
            if final == the_word[:-1]:
                print "==============================="
                print "==                           =="
                print "==         YOU WIN!          =="
                print "==                           =="
                print "==============================="
                return
            guess = raw_input("Guess a letter ->")
            if guess in the_word and guess not in letters_used:
                print "As it turns out, your guess was RIGHT!"
                letters_used += "," + guess if letters_used!="" else guess
                self.hangman_graphic(guesses)
                final = self.progress_updater(guess, the_word, progress)
                print "Progress: " + final
                print "Letter used: " + letters_used
            elif guess not in the_word and guess not in letters_used:
                if len(guess) > 1:
                    print "Please enter a single character!"
                    continue
                guesses += 1
                print "Things aren't looking so good, that guess was WRONG!"
                print "Oh man, that crowd is getting happy, I thought you"
                print "wanted to make them mad?"
                letters_used += "," + guess if letters_used!="" else guess
                self.hangman_graphic(guesses)
                print "Progress: " + "".join(progress)
                print "Letter used: " + letters_used
            else:
                print "That's the wrong letter, you wanna be out here all day?"
                print "Try again!"

    def hangman_graphic(self, guesses):
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
            print "|      0      "
            print "|             "
            print "|             "
            print "|             "
        elif guesses == 2:
            print "________      "
            print "|      |      "
            print "|      0      "
            print "|     /       "
            print "|             "
            print "|             "
        elif guesses == 3:
            print "________      "
            print "|      |      "
            print "|      0      "
            print "|     /|      "
            print "|             "
            print "|             "
        elif guesses == 4:
            print "________      "
            print "|      |      "
            print "|      0      "
            print "|     /|\     "
            print "|             "
            print "|             "
        elif guesses == 5:
            print "________      "
            print "|      |      "
            print "|      0      "
            print "|     /|\     "
            print "|     /       "
            print "|             "
        else:
            print "________      "
            print "|      |      "
            print "|      0      "
            print "|     /|\     "
            print "|     / \     "
            print "|             "
            print "The noose tightens around your neck, and you feel the"
            print "sudden urge to urinate."
            print "GAME OVER!"
            self.__init__()

    def progress_updater(self, guess, the_word, progress):
        i = 0
        while i < len(the_word):
            if guess == the_word[i]:
                progress[i] = guess
                i += 1
            else:
                i += 1

        return "".join(progress)

game = Hangman()
