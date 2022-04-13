

import sys
import math

def main():
    key_phrase = sys.stdin.readline().strip()
    plain_text = sys.stdin.readline().strip()
    key_phrase = key_phrase.replace(" ", "")
    plain_text = plain_text.replace(" ", "")
    key = []
    for i in key_phrase:
        if i not in key:
            key.append(i)
    for i in range(ord('a'), ord('z') + 1):
        if chr(i) not in key and chr(i) != 'q':
            key.append(chr(i))
    l = len(key)
    table = []
    for i in range(l):
        table.append(key[i:i+5])
    plain_text = list(plain_text)
    for i in range(len(plain_text) - 1): 
        if plain_text[i] == plain_text[i + 1]: 
            plain_text.insert(i + 1, 'x') 
    if len(plain_text) % 2 == 1:
        plain_text.append('x')
    plain_text = ''.join(plain_text)
    plain_text = [plain_text[i:i + 2] for i in range(0, len(plain_text), 2)]
    for i in plain_text:
        p1, p2 = i
        r1, r2 = 0, 0
        c1, c2 = 0, 0
        for j in range(5):
            for k in range(5):
                if table[j][k] == p1:
                    r1, c1 = j, k
                if table[j][k] == p2:
                    r2, c2 = j, k
        if r1 == r2:
            c1 = (c1 + 1) % 5
            c2 = (c2 + 1) % 5
        elif c1 == c2:
            r1 = (r1 + 1) % 5
            r2 = (r2 + 1) % 5
        else:
            c1, c2 = c2, c1
        print(table[r1][c1] + table[r2][c2], end='')

main()
