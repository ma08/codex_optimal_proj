

def sum_of_digits(n):
    return sum(map(int, str(n)))

def min_moves(n, s):
    moves = 0
    while sum_of_digits(n) > s:
        moves += 1
        n += 1
    return moves

t = int(input())
for i in range(t):
    n, s = map(int, input().split())
    print(min_moves(n, s))