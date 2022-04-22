


def solve(n):
    if n == 1:
        return 0
    moves = 0
    while n > 1:
        moves += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n += 1
    return moves

if __name__ == '__main__':
    n = int(input())
    print(solve(n))
