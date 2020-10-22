import random

# opening
print('''H A N G M A N
The game will be available soon.''')

rand_word()

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

def 