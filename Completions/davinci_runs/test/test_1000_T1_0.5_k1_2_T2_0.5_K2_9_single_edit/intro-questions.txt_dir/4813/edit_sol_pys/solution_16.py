
import sys
import random

word = str(input())
permutation = str(input())

# Check if Ned wins
def is_win(word, permutation):
    # Check if word contains letters not in permutation
    for letter in permutation:
        if letter not in word:
            return True
    return False

# Check if Ned loses
def is_lose(word, permutation):
    # Check if word contains letters from permutation
    for letter in word:
        if letter in permutation:
            return True
    return False

# Print result
if is_win(word, permutation):
    print("LOSE")
elif is_lose(word, permutation):
    print("WIN")
