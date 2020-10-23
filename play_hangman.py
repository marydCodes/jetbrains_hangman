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

def play_hangman():
    list_ = ['mississippi']
    tgt_word = random.choice(list_)
    tgt_len = len(tgt_word)
    print("-" * tgt_len)

    tries = 0
    while tries < 8:
        guess = input("Guess a letter: ")

        if guess in tgt_word:
            idxs = list(find_all(tgt_word, guess))
            print(f"Your guess appears at these places in the word: {idxs}.")
        else:
            print("That letter doesn't appear in the word.")
        tries += 1
    
    print('''
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