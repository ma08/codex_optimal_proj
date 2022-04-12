

#1 (correct)
"""
def rhyme(word, ending_lists):
    for ending_list in ending_lists:
        for ending in ending_list:
            if word.endswith(ending) or word.endswith(ending.lower()):
                return True
    return False

common_word = input()
ending_lists = []
for i in range(int(input())):
    ending_lists.append(input().split())
for i in range(int(input())):
    phrase = input().split()
    if len(phrase) == 2:
        if rhyme(phrase[0], ending_lists) and rhyme(phrase[1], ending_lists):
            print("YES")
        else:
            print("NO")
    else:
        if rhyme(phrase[1], ending_lists) and rhyme(phrase[2], ending_lists):
            print("YES")
        else:
            print("NO")
"""

#2 (wrong)
"""
import re

def rhyme(word, ending_lists):
    for ending_list in ending_lists:
        for ending in ending_list:
            if re.search(ending + "$", word) or re.search(ending.lower() + "$", word):
                return True
    return False

common_word = input()
ending_lists = []
for i in range(int(input())):
    ending_lists.append(input().split())
for i in range(int(input())):
    phrase = input().split()
    if len(phrase) == 2:
        if rhyme(phrase[0], ending_lists) and rhyme(phrase[1], ending_lists):
            print("YES")
        else:
            print("NO")
    else:
        if rhyme(phrase[1], ending_lists) and rhyme(phrase[2], ending_lists):
            print("YES")
        else:
            print("NO")
"""
