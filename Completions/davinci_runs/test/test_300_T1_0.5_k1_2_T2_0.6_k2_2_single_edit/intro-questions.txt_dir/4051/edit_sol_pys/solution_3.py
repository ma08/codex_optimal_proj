
from collections import Counter
from itertools import combinations
import sys

n = int(input())
arr = list(map(str, input().split()))

def check_anagrams(s1, s2):
    if Counter(s1) == Counter(s2):
        return True
    else:
        return False

def check_anagram_pairs(arr):
    anagram_pairs = []
    for word1, word2 in combinations(arr, 2):
        if check_anagrams(word1, word2):
            anagram_pairs.append((word1, word2))
    return anagram_pairs

print(check_anagram_pairs(arr))
