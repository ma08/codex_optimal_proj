

from collections import Counter

def is_multigram(word):
    # Check if the word is a multigram (return the root if it is, -1 if it isn't).
    # A multigram is a word that consists of concatenating two or more words
    # that are all mutually anagrams.
    # The first of these words is called the root of the multigram.
    # For instance, the word bbabab is a multigram with the root bba because
    # it consists of anagrams bba and bab.
    # Two words are mutually anagrams if one of them can be obtained from
    # the other by changing the letter order.
    # If there are multiple possible roots of the multigram, output the shortest.
    word_len = len(word)
    if word_len == 1:
        return word
    if word_len == 2:
        return -1
    for i in range(1, word_len//2 + 1):
        # Check if the first i characters are a root.
        # Check if the rest of the word is a root.
        if Counter(word[:i]) == Counter(word[i:]):
            return word[:i]
    return -1

if __name__ == "__main__":
    word = input()
    print(is_multigram(word))
