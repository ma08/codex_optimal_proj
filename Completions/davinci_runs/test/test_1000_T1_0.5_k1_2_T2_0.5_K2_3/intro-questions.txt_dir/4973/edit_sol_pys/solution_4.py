import random

def guess(x):
    guess = random.randint(1, x)
    print(guess)
    if guess == x:
        return True
    else:
        return False

x = int(input())
while not guess(x):
    pass
