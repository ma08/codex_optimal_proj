

import sys
import re

def brainfuck(s):
    s = s.split('+')
    for i in range(len(s)):
        s[i] = s[i].split('-')
    #print(s)
    res = ''
    for i in range(len(s)):
        if len(s[i]) > 1:
            res += '>'*int(s[i][0]) + '<'*int(s[i][1])
        else:
            res += '>'*int(s[i][0])
    res += '<'*len(s)
    res += '[<+>-]<'
    res += '>'
    res += '.'
    return res

s = sys.stdin.readline().strip()
print(brainfuck(s))