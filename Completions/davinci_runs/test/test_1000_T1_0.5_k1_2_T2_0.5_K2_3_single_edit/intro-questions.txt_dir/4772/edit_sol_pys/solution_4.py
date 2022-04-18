

R, C = map(int, input().split())
crossword = []
for i in range(R):
    crossword.append(list(input()))

    """
    Checks if there are any two contiguous letters in any row
    """
def check_horizontal(crossword, R, C):
    for r in range(R):
        for c in range(C - 1):
            if crossword[r][c].isalpha() and crossword[r][c + 1].isalpha():
                return True
    return False

    """
    Checks if there are any two contiguous letters in any column
    """
def check_vertical(crossword, R, C):
    for c in range(C):
        for r in range(R - 1):
            if crossword[r][c].isalpha() and crossword[r + 1][c].isalpha():
                return True
    return False

def get_horizontal(crossword, R, C):
    """
    Returns the two contiguous letters in any row
    """
    for r in range(R):
        for c in range(C - 1):
            if crossword[r][c].isalpha() and crossword[r][c + 1].isalpha():
                return crossword[r][c] + crossword[r][c + 1]

def get_vertical(crossword, R, C):
    """
    Returns the two contiguous letters in any column
    """
    for c in range(C):
        for r in range(R - 1):
            if crossword[r][c].isalpha() and crossword[r + 1][c].isalpha():
                return crossword[r][c] + crossword[r + 1][c]

if check_horizontal(crossword, R, C):
    print(get_horizontal(crossword, R, C))
else:
    print(get_vertical(crossword, R, C))
