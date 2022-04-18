
#!/bin/python3
import sys

S = input().strip()

dict_ = {'R': 'RUD', 'U': 'URD', 'L': 'LUD', 'D': 'DRU'}


def takahashi_dance(s):
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] not in dict_['L']:
                return 'No'
        elif s[i] not in dict_['R']:
            return 'No'
    return 'Yes'

print(takahashi_dance(S))
