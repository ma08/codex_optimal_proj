

R, C = map(int, input().split())

crossword = []
for _ in range(R):
    crossword.append(input())

lex_max = '~'

for i in range(R):
    for j in range(C):
        if crossword[i][j] == '#':
            continue
        if j < C - 1 and crossword[i][j + 1] != '#':
            lex_max = max(lex_max, crossword[i][j:j + 2], key=lambda x: (x[0], x[1]))
        if i < R - 1 and crossword[i + 1][j] != '#':
            lex_max = max(lex_max, crossword[i][j] + crossword[i + 1][j], key=lambda x: (x[0], x[1]))

print(lex_max)
