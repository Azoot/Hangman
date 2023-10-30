# Hangman Game

## Introduction

The Hangman Game is a simple Python script that allows you to play the classic word-guessing game "Hangman" in the command line. You'll be presented with a secret word, and you must guess individual letters to complete the word while having a limited number of lives. The goal is to guess the word before running out of lives.

## Features

- Randomly selects a secret word.
- Provides a graphical representation of the player's remaining lives.
- Tracks and displays used letters.
- Informs you when you've already used a particular letter.
- Determines win or loss conditions and displays the result.

## Requirements

- Python 3.x

## How to Play

1. Open a command prompt or terminal.

2. Navigate to the directory where the script is located.

3. Run the script by executing the following command:

   ```bash
   python hangman.py


- 1. The game will begin, and you will see a series of underscores representing the letters of the secret word. You have 10 lives.

- 2. Guess a letter by entering it and pressing Enter. If the letter is in the word, it will be revealed; otherwise, you will lose a life.

- 3. Continue guessing letters until you either complete the word or run out of lives.

- 4. If you want to quit the game, type "quit" and press Enter.

- 5. After the game ends, you will be notified whether you won or lost.

## Customization
- You can customize the list of words in the WORDS variable at the beginning of the script. This variable is used for testing short words.

- You can change the initial secret word by modifying the WORDSy variable, which is used to test words with space separators.


## Additional Scripts
- test.py: This script serves as a test or development variant. It selects a random word from a file and displays missed letters, correct letters, and a Hangman figure.

- testing.py: Similar to test.py, this script is another variant that uses a predefined list of words and displays a Hangman figure based on incorrect guesses.


## Variants and Test Scripts

In addition to the main Hangman game, there are two additional code variants and test scripts that demonstrate different approaches to creating a Hangman game:

- test.py: This script serves as a test or development variant. It selects a random word from a file and displays missed letters, correct letters, and a Hangman figure.

- testing.py: Similar to test.py, this script is another variant that uses a predefined list of words and displays a Hangman figure based on incorrect guesses.
