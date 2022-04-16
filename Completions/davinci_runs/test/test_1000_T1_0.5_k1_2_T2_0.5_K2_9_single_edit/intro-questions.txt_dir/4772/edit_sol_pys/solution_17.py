
R, C = map(int, input().split())
crossword = [input() for i in range(R)]

def check_horizontal(crossword, R, C):
    for r in range(R):
        for c in range(C - 1):
            if crossword[r][c].isalpha() and crossword[r][c + 1].isalpha():
                return True
    return False

def check_vertical(crossword, R, C):
    for c in range(C):
        for r in range(R - 1):
            if crossword[r][c].isalpha() and crossword[r + 1][c].isalpha():
                return True
    return False

def get_horizontal(crossword, R, C):
    for r in range(R):
        for c in range(C - 1):
            if crossword[r][c].isalpha() and crossword[r][c + 1].isalpha():
                return ''.join(crossword[r][c:c + 2])

def get_vertical(crossword, R, C):
    for c in range(C):
        for r in range(R - 1):
            if crossword[r][c].isalpha() and crossword[r + 1][c].isalpha():
                return ''.join(list(map(lambda x: x[c], crossword[r:r + 2])))

if check_horizontal(crossword, R, C):
    print(get_horizontal(crossword, R, C))
else:
    print(get_vertical(crossword, R, C))
