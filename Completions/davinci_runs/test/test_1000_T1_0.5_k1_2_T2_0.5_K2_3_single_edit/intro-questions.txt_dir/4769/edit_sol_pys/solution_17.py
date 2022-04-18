

from collections import Counter

def is_multigram(word):
    # check if the word is a multigram (return the root if it is, -1 if it isn't)
    # a multigram is a word that consists of concatenating two or more words
    # that are all mutually anagrams
    # the first of these words is called the root of the multigram
    # for instance, the word bbabab is a multigram with the root bba because
    # it consists of anagrams bba and bab
    # two words are mutually anagrams if one of them can be obtained from
    # the other by changing the letter order
    # if there are multiple possible roots of the multigram, output the shortest
    pass

if __name__ == "__main__":
    word = input()
    print(is_multigram(word))
