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