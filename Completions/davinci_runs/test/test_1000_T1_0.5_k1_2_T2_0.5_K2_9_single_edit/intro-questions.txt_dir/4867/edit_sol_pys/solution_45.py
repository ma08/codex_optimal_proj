

# Getting input
M, N = [int(x) for x in input().split()]  # M is number of rows, N is number of columns
U, L, R, D = [int(x) for x in input().split()]  # U is number of rows above the crossword, L is number of columns left of the crossword, R is number of columns right of the crossword, D is number of rows below the crossword

# Creating the crossword
crossword = [input() for x in range(M)]

# Creating the frame
frame = []
for i in range(U):
    frame.append("#."*(N+L+R-1)+"#")
frame.append("."*L+crossword[0]+"."*R)
for i in range(1, M):
    frame.append("."*L+crossword[i]+"."*R)
for i in range(D):
    frame.append("#."*(N+L+R-1)+"#")

# Printing the frame
for line in frame:
    print(line)
