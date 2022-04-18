
import sys
import random

# Check if Ned wins
def is_win(word, permutation):
    # Check if word contains letters from permutation
    for letter in permutation:
        if letter in word:
            return True
    return False

# Check if Ned loses
def is_lose(word, permutation):
    # Check if word contains letters not in permutation
    for letter in word:
        if letter not in permutation:
            return True
    return False

# Print result
if is_win(sys.argv[1], sys.argv[2]):
    print("WIN")
elif is_lose(sys.argv[1], sys.argv[2]):
    print("LOSE")
