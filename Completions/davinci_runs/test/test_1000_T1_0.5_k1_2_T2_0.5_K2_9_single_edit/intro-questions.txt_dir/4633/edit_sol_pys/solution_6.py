
def sum_of_digits(n):
    return sum(map(int, str(n)))


def min_moves(n, s, i):
    moves = 0
    while sum_of_digits(n) > s:
        moves += 1
        n = n + (10**i)

    return moves

t = int(input())
for i in range(t):
    n, s = map(int, input().split())
    i = 0
    while sum_of_digits(n) > s:
        i += 1
        n = n + (10**i)
    print(min_moves(n, s, i))
