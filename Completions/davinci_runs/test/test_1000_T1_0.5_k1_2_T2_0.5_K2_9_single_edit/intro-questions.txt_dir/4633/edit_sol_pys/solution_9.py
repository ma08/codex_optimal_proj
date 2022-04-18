

def sumOfDigits(n):
    sum = 0
    for i in n:
        sum += int(i)
    return sum

def getMinMoves(n):
    n = str(n) # convert to string
    nSum = sumOfDigits(n)
    if nSum <= s: # if sum of digits is less than s
        return 0
    else:
        moves = 0
        i = 0
        while nSum > s:
            if i == len(n) - 1:
                n = str(int(n) + 1) # increase the number by 1
                i = 0
                moves += 1
            else:
                n = n[:i] + str(int(n[i]) - 1) + n[i+1:]
                i += 1
            nSum = sumOfDigits(n)
        return moves

t = int(input())

for i in range(t):
    n, s = map(int, input().split())
    print(getMinMoves(n))
