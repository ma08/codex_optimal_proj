#!/usr/bin/python3

R, C = map(int, input().split())

crossword = []
for _ in range(R):
    crossword.append(input())

lex_min = '~'

for i in range(R):
    for j in range(C):
        if crossword[i][j] == '#':
            continue
        if j < C - 1 and crossword[i][j + 1] != '#':
            lex_min = min(lex_min, crossword[i][j:j + 2])
        if i < R - 1 and crossword[i + 1][j] != '#':
            lex_min = min(lex_min, crossword[i][j] + crossword[i + 1][j])

print(lex_min)
