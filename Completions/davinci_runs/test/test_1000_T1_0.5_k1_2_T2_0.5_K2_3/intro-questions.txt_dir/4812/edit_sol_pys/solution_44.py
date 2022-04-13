

#1:
"""
def rhyme(word, suffix_lists):
    for suffix_list in suffix_lists:
        for suffix in suffix_list:
            if word.endswith(suffix):
                return True
    return False

common_word = input()
suffix_lists = []
for i in range(int(input())):
    suffix_lists.append(input().split())
for i in range(int(input())):
    phrase = input().split()
    if len(phrase) == 2:
        if rhyme(phrase[0], suffix_lists) and rhyme(phrase[1], suffix_lists):
            print("YES")
        else:
            print("NO")
    else:
        if rhyme(phrase[1], suffix_lists) and rhyme(phrase[2], suffix_lists):
            print("YES")
        else:
            print("NO")
"""

#2:
"""
import re

def rhyme(word, suffix_lists):
    for suffix_list in suffix_lists:
        for suffix in suffix_list:
            if re.search(suffix + "$", word):
                return True
    return False

common_word = input()
suffix_lists = []
for i in range(int(input())):
    suffix_lists.append(input().split())
for i in range(int(input())):
    phrase = input().split()
    if len(phrase) == 2:
        if rhyme(phrase[0], suffix_lists) and rhyme(phrase[1], suffix_lists):
            print("YES")
        else:
            print("NO")
    else:
        if rhyme(phrase[1], suffix_lists) and rhyme(phrase[2], suffix_lists):
            print("YES")
        else:
            print("NO")
"""
