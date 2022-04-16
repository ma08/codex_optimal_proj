
# Getting input
M, N = [int(x) for x in input().split()]
U, L, R, D = [int(x) for x in input().split()]

# Creating the crossword
crossword = [input() for x in range(M)]

# Creating the frame
frame = []
for i in range(U):
    frame.append("#." * (N + L + R - 1) + "#")
frame.append("." * L + crossword[0] + "." * R)
for i in range(1, M):
    frame.append("." * L + crossword[i] + "." * R)
for i in range(D):
    frame.append("#." * (N + L + R - 1) + "#")

# Printing the frame
for line in frame:
    print(line)
