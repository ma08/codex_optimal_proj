
import sys
import string

# Read the input
input_lines = sys.stdin.readlines()

# Initialize the board
board = []
for i in range(8):
    board.append(input_lines[i+1][1:9])

# Initialize the board positions
pieces = {'K': 'K', 'Q': 'Q', 'R': 'R', 'B': 'B', 'N': 'N', 'P': '', 'k': 'k', 'q': 'q', 'r': 'r', 'b': 'b', 'n': 'n', 'p': ''}

# Initialize the white pieces
white_pieces = []
for i in range(8):
    for j in range(8):
        if board[i][j] in pieces.keys():
            if board[i][j] in ['K', 'Q', 'R', 'B', 'N', 'P']:
                white_pieces.append(pieces[board[i][j]] + string.lowercase[j] + str(8-i))

# Initialize the black pieces
black_pieces = []
for i in range(8):
    for j in range(8):
        if board[i][j] in pieces.keys():
            if board[i][j] in ['k', 'q', 'r', 'b', 'n', 'p']:
                black_pieces.append(pieces[board[i][j]] + string.lowercase[j] + str(8-i))

# Print the output
print "White: " + ','.join(white_pieces)
print "Black: " + ','.join(black_pieces)
