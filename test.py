import random
import os


def clear_screen(): return os.system("cls")

# print(random.choice(open("WordsForGames.txt").readline().split())) <--- uproszczona opcja wyboru slowa z losowej lini

lives = 10
quit = "Hah...female off a cat. You call yourself Human!"
used_letters = ''
letters_in_word = ''


def random_word():
    with open("WordsForGames.txt", 'r')as word_file:
        lines = word_file.readlines()
        words = random.choice(lines).split("|")
        random_word = random.choice(words).strip().lower()
        hiden_word = random_word
        print("random: ", random_word)
        print("hiden: ", hiden_word)
        clear_screen()
        print(f"\n\nYou can start guessing")
    return hiden_word

def front_screen_menu():
    print("нⷩaͣngmͫaͣn" * 9)
    print("██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗нⷩ\n██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║n\n███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║g\n██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║mͫ\n██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║aͣ\n╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝n")

def choose_difficulty():
    difficulty = input("Choose young padawan: \n1. Eazy. \n2. Medium\n3. Hard \nSo hows it gonna be: ")
    if difficulty == "1":
        lives = 10
    elif difficulty == "2":
        lives = 6
    elif difficulty == "3":
        lives = 4
    elif difficulty == "quit":
        print(quit)
        exit(0)

def players_lives_graf():
    print("\u2764  " * lives)
    return lives

def get_letter(guessed_letter):
    while True:
        letter = input("Gimmee lettaaaa: ").lower()
        if letter == 'quit':
            print(quit)
            break
        elif len(letter) != 1:
            print('Please, please... a LETTER! SINGLE!')
        elif letter in guessed_letter:
            print("You have already guessed that letter. Choose again")
        elif letter not in 'abcdefghijklmnopqrstuvwxyz':
            print('Gooosh a LETTER !')
        else:
            return letter

def display(used_letters, letters_in_word, hiden_word):
    underscores = '_' * len(hiden_word)    
    if used_letters or letters_in_word:    
        print('Used letters: ', end='')
        for letter in used_letters:
            if letter in used_letters:
                print(letter, end="-")
        print()
            # Filing up correctly guessed letters.
        for i in range(len(hiden_word)):
            if hiden_word[i] in letters_in_word:
                underscores = underscores[:i] + hiden_word[i] + underscores[i+1:]
        for letter in underscores:
            print(letter, end="")
        print()

def play():
    front_screen_menu()
    choose_difficulty()
    hiden_word = random_word()
    used_letters = ''
    letters_in_word = ''
    gused_letters = ''
    while True:
        display(used_letters, letters_in_word, hiden_word)
            # Ask player for letter (input)
        letter = get_letter(used_letters + letters_in_word)
        clear_screen()
        if letter in hiden_word:
            letters_in_word = letters_in_word + letter

                # Check if player won.
            for i in range(len(hiden_word)):
                if hiden_word[i] not in letters_in_word:
                    break
            if len(hiden_word) == len(gused_letters):
                print(f'Yeah... thats the thing youre looking for: {hiden_word}')

            else:
                gused_letters = gused_letters + letter

        used_letters = used_letters + letter
            # Check if player has guessed too many times and lost.
        if len(gused_letters) == len(word_to_print) - 1:
            display(used_letters, letters_in_word, hiden_word)


word_to_print = list(random_word().capitalize())
clear_screen()
play()