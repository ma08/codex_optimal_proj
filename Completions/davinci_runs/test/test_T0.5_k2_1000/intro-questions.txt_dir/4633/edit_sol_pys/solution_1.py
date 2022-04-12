
def sumOfDigits(n):
    return sum(map(int,str(n)))

def minMoves(n, s):
    moves = 0
    while sumOfDigits(n) > s:
        moves += 1
        n += 1
    return moves

t = int(input())
for i in range(t):
    n,s = map(int,input().split())
    print(minMoves(n, s))
