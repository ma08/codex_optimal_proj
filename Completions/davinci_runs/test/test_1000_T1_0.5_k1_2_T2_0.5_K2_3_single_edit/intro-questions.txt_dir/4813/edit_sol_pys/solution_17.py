

import sys
import random

word = input()
permutation = input()

# Check if Ned can win
def is_win(word, permutation):
    # Check if word contains letters from permutation
    for letter in permutation:
        if letter in word:
            return True
    return False

# Check if Ned can lose
def is_lose(word, permutation):
    # Check if word contains letters not in permutation
    for letter in word:
        if letter not in permutation:
            return True
    return False

# Print result
if is_win(word, permutation):
    print("WIN")
elif is_lose(word, permutation):
    print("LOSE")
