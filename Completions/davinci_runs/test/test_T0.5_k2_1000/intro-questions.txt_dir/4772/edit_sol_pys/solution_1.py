R, C = map(int, input().split())
crossword = []
for i in range(R):
    crossword.append(input())

def check_horizontal(crossword, R, C):
    for r in range(R):
        for c in range(C - 1):
            if crossword[r][c].isalpha() and crossword[r][c + 1].isalpha() and crossword[r][c] != crossword[r][c + 1]:
                return True
    return False

def check_vertical(crossword, R, C):
    for c in range(C):
        for r in range(R - 1):
            if crossword[r][c].isalpha() and crossword[r + 1][c].isalpha() and crossword[r][c] != crossword[r + 1][c]:
                return True
    return False

def get_horizontal(crossword, R, C):
    for r in range(R):
        for c in range(C - 1):
            if crossword[r][c].isalpha() and crossword[r][c + 1].isalpha() and crossword[r][c] != crossword[r][c + 1]:
                return crossword[r][c] + crossword[r][c + 1]

def get_vertical(crossword, R, C):
    for c in range(C):
        for r in range(R - 1):
            if crossword[r][c].isalpha() and crossword[r + 1][c].isalpha() and crossword[r][c] != crossword[r + 1][c]:
                return crossword[r][c] + crossword[r + 1][c]

if check_horizontal(crossword, R, C):
    print(get_horizontal(crossword, R, C))
else:
    print(get_vertical(crossword, R, C))
