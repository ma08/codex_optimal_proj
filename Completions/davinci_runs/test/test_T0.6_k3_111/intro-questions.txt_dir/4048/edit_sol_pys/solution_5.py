
# get input
N = int(input())

# determine the minimum number of moves to reach a square that contains N grains
moves = 0
while N > 1:
    if N % 2 == 0:
        N = N // 2
    else:
        N -= 1
    moves += 1

# print the minimum number of moves
print(moves)
