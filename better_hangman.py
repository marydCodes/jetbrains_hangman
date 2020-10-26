import random

tgt_word = random.choice(['python', 'java', 'kotlin', 'javascript'])
hint = list('-' * len(tgt_word))
tries = 0

print('H A N G M A N')

while tries < 8:
    print()
    print("".join(hint))

    if '-' not in hint:
        print("You guessed the word!\nYou survived!")
        break

    guess = input("Input a letter: ")

    if guess not in tgt_word:
        print("That letter doesn't appear in the word")
        tries += 1

    else:
        if guess in hint:
            print("No improvements")
            tries +=1

        for i in range(len(tgt_word)):
            if guess == tgt_word[i]:
                hint[i] = guess

else:
    print('You lost!')