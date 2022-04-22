
def min_moves(n, m):
    x, y = 1, 1
    moves = 0
    while True:
        moves += 1
        if n * m == x * y:
            return moves
        elif n * m < x * y:
            y -= 1
            x += 1
        else:
            x += 1


def main():
    n, m = map(int, input().split())
    print(min_moves(n, m))


if __name__ == '__main__':
    main()
