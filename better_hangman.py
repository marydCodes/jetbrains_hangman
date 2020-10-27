import random
import string

# opening
print("H A N G M A N")
play = str(input("Type 'play' to play the game, 'exit' to quit: "))

tgt_word = random.choice(['python', 'java', 'kotlin', 'javascript'])
hint = list('-' * len(tgt_word))
lives = 8
store_guesses = set()

while lives > 0:
    print()
    print("".join(hint))

    if '-' not in hint:
        print("You guessed the word!\nYou survived!")
        break

    guess = input("Input a letter: ")

    if len(guess) != 1:
        print("You should input a single letter")
    elif guess not in string.ascii_lowercase:
        print("Please enter a lowercase English letter")
    elif guess in store_guesses:
        print("You've already guessed this letter")

    else:
        if guess in tgt_word:
            for i in range(len(tgt_word)):
                if guess == tgt_word[i]:
                    hint[i] = guess
        else:
            print("That letter doesn't appear in the word")
            lives -= 1
    store_guesses.add(guess)
else:
    print('You lost!')