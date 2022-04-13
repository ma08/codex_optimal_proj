

import sys
import math

#sys.stdin = open("sample.txt", "r")

table = {
    'a': '@',
    'b': '8',
    'c': '(',
    'd': '|)',
    'e': '3',
    'f': '#',
    'g': '6',
    'h': '[-]',
    'i': '|',
    'j': '_|',
    'k': '|<',
    'l': '1',
    'm': '[]\\/[]',
    'n': '[]\\[]',
    'o': '0',
    'p': '|D',
    'q': '(,)',
    'r': '|Z',
    's': '$',
    't': "']['", #']['
    'u': '|_|',
    'v': '\/',
    'w': '\/\/',
    'x': '}{',
    'y': '`/',
    'z': '2',
    'A': '@',
    'B': '8',
    'C': '(',
    'D': '|)',
    'E': '3',
    'F': '#',
    'G': '6',
    'H': '[-]',
    'I': '|',
    'J': '_|',
    'K': '|<',
    'L': '1',
    'M': '[]\\/[]',
    'N': '[]\\[]',
    'O': '0',
    'P': '|D',
    'Q': '(,)',
    'R': '|Z',
    'S': '$',
    'T': "']['",
    'U': '|_|',
    'V': '\/',
    'W': '\/\/',
    'X': '}{',
    'Y': '`/',
    'Z': '2'
}

line = sys.stdin.readline()

for i in line:
    if i in table:
        print(table[i], end='')
    else:
        print(i, end='')
