

from collections import Counter, defaultdict

def is_multigram(word):
    # check if the word is a multigram (return the root if it is, -1 if it isn't)
    # a multigram is a word that consists of concatenating two or more words,
    # all mutually anagrams
    # the first of these words is called the root of the multigram
    # for instance, the word bbabab is a multigram with the root bba,
    # because it consists of anagrams bba and bab
    # two words are mutually anagrams if one of them can be obtained from
    # the other by changing the letter order
    # if there are multiple possible roots of the multigram, output the shortest one
    word_len = len(word)
    if word_len == 1:
        return word
    if word_len == 2:
        return -1
    for i in range(1, word_len//2 + 1):
        # check if the first i characters are a root
        # check if the rest of the word is a root
        if Counter(word[:i]) == Counter(word[i:]):
            return word[:i]
    return -1

def print_anagrams(words):
    # print all anagrams of the words in the list words
    # anagrams are words that consist of the same letters
    # for instance, the words bba and bab are anagrams
    # all anagrams should be printed in alphabetical order
    # each group of anagrams should be printed on a new line
    # each group of anagrams should be sorted in alphabetical order
    # each group should be printed in the format "word1 word2 word3 ..."
    # where word1 is the first word in the group, word2 is the second word, etc
    # if there are no anagrams, print nothing
    # hint: you can use the function is_anagram from the previous question
    # hint: you can use the function is_anagram from the previous question
    anagrams = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        anagrams[key].append(word)
    for key in sorted(anagrams.keys()):
        print(' '.join(sorted(anagrams[key])))

if __name__ == "__main__":
    words = input().split()
    print_anagrams(words)
