

def sum_of_digits(n):
    sum_ = 0
    for i in n:
        sum_ += int(i)
    return sum_

def get_min_moves(n):
    n = str(n)
    nSum = sum_of_digits(n)
    if nSum <= s:
        return 0
    else:
        moves = 0
        i = 0
        while nSum > s:
            if i == len(n) - 1:
                n = str(int(n) + 1)
                i = 0
                moves += 1
            else:
                n = n[:i] + str(int(n[i]) - 1) + n[i+1:]
                i += 1
            nSum = sum_of_digits(n)
        return moves

t = int(input())

for i in range(t):
    n, s = map(int, input().split())
    print(get_min_moves(n))
