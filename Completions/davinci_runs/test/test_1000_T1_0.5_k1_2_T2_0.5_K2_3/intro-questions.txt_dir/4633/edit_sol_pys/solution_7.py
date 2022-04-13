
def sumOfDigits(n):
    s = 0
    for i in n:
        s += int(i)
    return s

def getMinMoves(n):
    n = str(n)
    n_s = sumOfDigits(n)
    if n_s <= s:
        return 0
    else:
        moves = 0
        i = 0
        while n_s > s:
            if i == len(n) - 1:
                n = str(int(n) + 1)
                i = 0
                moves += 1
            else:
                n = n[:i] + str(int(n[i]) - 1) + n[i+1:]
                i += 1
            n_s = sumOfDigits(n)
        return moves

t = int(input())

for i in range(t):
    n, s = map(int, input().split())
    print(getMinMoves(n))
