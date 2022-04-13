
def sumOfDigits(n):
    return sum(map(int, str(n)))


def minMoves(n, s, n):
    moves = 0
    while sumOfDigits(n) > s:
        moves += 1
        n += 1
    return moves


n, s = map(int, input().split())
print(minMoves(n, s))
