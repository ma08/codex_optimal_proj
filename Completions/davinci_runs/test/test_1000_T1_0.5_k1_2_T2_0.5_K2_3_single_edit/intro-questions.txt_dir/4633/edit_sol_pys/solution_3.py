
def getMinMoves(n, s):
    moves = 0
    while n > 0:
        if n % 10 == 0:
            n -= 1
            moves += 1
        else:
            n -= n % 10
            moves += n % 10
    return moves

t = int(input())

for i in range(t):
    n, s = map(int, input().split())
    print(getMinMoves(n, s))
