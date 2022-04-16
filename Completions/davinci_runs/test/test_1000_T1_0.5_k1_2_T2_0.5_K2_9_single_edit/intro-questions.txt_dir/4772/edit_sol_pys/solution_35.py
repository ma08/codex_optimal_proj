# https://www.hackerrank.com/challenges/crossword-puzzle/problem


def find_words(board, words):
    # find all the locations of the first word
    word = words[0]
    locations = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == word[0]:
                locations.append((i, j))
    # check if the word can be placed in the board
    for location in locations:
        if check_word(board, word, location):
            # if it can, add it to the board
            add_word(board, word, location)
            # if this is the last word, return the board
            if len(words) == 1:
                return board
            # otherwise, try to find the next word
            result = find_words(board, words[1:])
            if result is not None:
                return result
            # if it didn't work, remove the word from the board
            remove_word(board, word, location)
    # if none of the locations worked, return None
    return None

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
