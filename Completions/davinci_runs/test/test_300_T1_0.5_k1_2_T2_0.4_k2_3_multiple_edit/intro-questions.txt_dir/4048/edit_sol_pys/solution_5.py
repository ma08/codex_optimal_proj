def min_moves(n):
    x, y = 0, 0
    moves = 0
    while True:
        moves += 1
        if n == (x + 1) * (y + 1):
            return moves
        elif n < (x + 1) * (y + 1):
            y -= 1
            x += 1
        else:
            x += 1


def main():
    n = int(input())
    print(min_moves(n))


if __name__ == '__main__':
    main()
