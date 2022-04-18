

#1
"""
def rhyme(word, ending_lists):
    for ending_list in ending_lists:
        for ending in ending_list:
            if word.endswith(ending):
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

#2
"""
import re

def rhyme(word, ending_lists):
    for ending_list in ending_lists:
        for ending in ending_list:
            if re.search(ending + "$", word):
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

#3

import re

def rhyme(word, ending_lists):
    for ending_list in ending_lists:
        for ending in ending_list:
            if re.search(ending + "$", word):
                return True
    return False

def rhyme_check(phrase, ending_lists):
    if len(phrase) == 2:
        if rhyme(phrase[0], ending_lists) and rhyme(phrase[1], ending_lists):
            return "YES"
    else:
        if rhyme(phrase[1], ending_lists) and rhyme(phrase[2], ending_lists):
            return "YES"
    return "NO"

common_word = input()
ending_lists = []
for i in range(int(input())):
    ending_lists.append(input().split())
for i in range(int(input())):
    phrase = input().split()
    print(rhyme_check(phrase, ending_lists))
