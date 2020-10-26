import random

# opening
print('''H A N G M A N
''')

# supplementary function
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

# game code
def play_hangman():
    list_ = ['python', 'java', 'kotlin', 'javascript']
    tgt_word = random.choice(list_)     # randomly choose a word
    hint = "-" * len(tgt_word)
    print(hint)

    lives = 8
    store_guesses = []
    while lives > 0:
        guess = input("Input a letter: ")

        if guess in tgt_word:
            if guess in store_guesses:
                print("No improvements")
                print("\n")
                print(hint)
                lives -= 1
            else:
                hint_list = list(hint)
                idxs = list(find_all(tgt_word, guess))
                for i in idxs:
                    hint_list[i] = guess
                hint = ''.join(hint_list)
                print("\n")
                print(hint)
                store_guesses.append(guess)
        else:
            print("That letter doesn't appear in the word.")
            print("\n")
            print(hint)
            lives -= 1
    
    print('''
You have no more lives left.

Thanks for playing! 
We'll see how well you did in the next stage''')

play_hangman()