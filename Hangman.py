import os
from random import choice
from copy import copy

def clear_screen(): return os.system("cls")

WORDS = ['worm', 'nothing', 'something', 'keyboard', 'lir', 'dry', 'trr', 'see', 'pneumonoultramicroscopicsilicovolcanoconiosis', 'antidisestablishmentarianism', 'tree',]
WORDSy = 'Jan Kowalski'


class Hangman():
    def __init__(self):
        self.word = ""
        self.letters = []
        self.lives = 10
        self.used = []
        self.a_set = set()


    def __players_lives_graf(self):
        print("\u2764  " * self.lives)
        return self.lives


    def play(self):

        self.__choose_random_word()
        self.__print_result()

        while self.__player_lives() and self.__letters_in_word():
            _l = input('Input letter: ')
            _l = _l.lower()
            if _l == "quit":
                self.lives = 0
                break

            
            if _l in self.letters and _l not in self.used:
                self.letters = list(filter(_l.__ne__, self.letters)) 
                self.__used_letters(_l)
                self.__print_result()
            elif _l not in self.used and _l not in self.letters:
                self.__used_letters(_l)
                self.lives -= 1
                self.__print_result()
            elif _l in self.used or _l in self.letters:
                self.__alt_print_result()
            else:
                self.__print_result()

        if self.__player_lives():
            print("You Win!")
        else:
            print("You Lose!")


    def __used_letters(self, _letter):
        if _letter not in self.used:
            self.used.append(_letter)


    def __alt_res(self):
        if not self.used:
            print('\n')
        else:
            print('\n',self.used)


    def __print_result(self):
        clear_screen()

        print(f'Player Lives:  {self.__players_lives_graf()}\n')

        for letter in self.word:
            if letter not in self.letters:
                print(f" {letter} ", end="")
            else:
                print(" _ ", end="")     

        self.__alt_res()


    def __alt_print_result(self):
        clear_screen()

        print(f'Player Lives:  {self.__players_lives_graf()}\n')

        for letter in self.word:
            if letter not in self.letters:
                print(f" {letter} ", end="")
            else:
                print(" _ ", end="")

        print("\n You used that letter already\n")
        print(self.used)


    def __player_lives(self) -> bool:
        return self.lives > 0


    def __letters_in_word(self) -> bool:
        return len(self.letters)


    def __choose_random_word(self): 
        self.word = choice(WORDS)
        self.letters = copy(self.word)
        self.a_set = set(self.word)


game = Hangman()

game.play()