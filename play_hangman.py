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
    list_ = ['java']             # list of words to choose from
    tgt_word = random.choice(list_)     # randomly choose a word
    w = "-" * len(tgt_word)
    print(w)

    lives = 8
    store_guesses = []
    while lives > 0:
        guess = input("Input a letter: ")

        if guess in tgt_word:
            if guess in store_guesses:
                print("No improvements")
                print("\n")
                print(w)
                lives -= 1
            else:
                wl = list(w)
                idxs = list(find_all(tgt_word, guess))
                for i in idxs:
                    wl[i] = guess
                w = ''.join(wl)
                print("\n")
                print(w)
                store_guesses.append(guess)
        else:
            print("That letter doesn't appear in the word.")
            print("\n")
            print(w)
            lives -= 1
    
    print('''
You have no more lives left.

Thanks for playing! 
We'll see how well you did in the next stage''')

# intermediary practice
def guess_sgl_word():
    guess = str(input("Guess the word: "))
    if guess == "python":
        print("You survived!")
    else:
        print("You lost!")

def rand_word():
    list_ = ['python', 'java', 'kotlin', 'javascript']
    target_word = random.choice(list_)
    
    guess = str(input("Guess the word: "))
    if guess == target_word:
        print("You survived!")
    else:
        print("You lost!")

def rand_word_hint():
    list_ = ['python', 'java', 'kotlin', 'javascript']
    target_word = random.choice(list_)
    
    tgt_len = len(target_word)
    hint = target_word[0:3] + ("-" * (len(target_word) - 3))
    
    guess = str(input(f"Guess the word {hint}: "))
    if guess == target_word:
        print("You survived!")
    else:
        print("You lost!")

### FUNCTION CALLS ###
# guess_sgl_word()
# rand_word()
# rand_word_hint()
play_hangman()