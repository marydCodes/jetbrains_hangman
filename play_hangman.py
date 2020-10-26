import random

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
    # opening
    print("H A N G M A N")

    list_ = ['python', 'java', 'kotlin', 'javascript']
    # list_ = ['java']
    tgt_word = random.choice(list_)     # randomly choose a word
    hint = "-" * len(tgt_word)
    print(hint)

    lives = 8
    while lives > 0:
        guess = input("Input a letter: ")

        if guess in tgt_word:
            if guess in hint:
                print("No improvements")
                lives -= 1
            else:
                hint_list = list(hint)
                idxs = list(find_all(tgt_word, guess))
                for i in idxs:
                    hint_list[i] = guess
                hint = ''.join(hint_list)
                print(hint)
        else:
            print("That letter doesn't appear in the word.")
            lives -= 1
    else:
        print("You lost!")

play_hangman()