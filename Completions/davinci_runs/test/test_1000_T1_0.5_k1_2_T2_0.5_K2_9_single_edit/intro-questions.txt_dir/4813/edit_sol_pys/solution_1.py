

word = input()
permutation = input()

# Check if Ned wins
def is_win(word, permutation):
    # Check if word contains letters from permutation
    for letter in permutation:
        if letter in word:
            return "WIN"
    return "LOSE"

# Check if Ned loses
def is_lose(word, permutation):
    # Check if word contains letters not in permutation
    for letter in word:
        if letter not in permutation:
            return "LOSE"
    return "WIN"

# Print result
print(is_win(word, permutation))
