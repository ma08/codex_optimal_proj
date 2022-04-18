def min_moves(n):
    x, y = 1, 1
    moves = 0
    while True:
        moves += 1
        if x * y == n:
            return moves
        elif x * y > n:
            y -= 1
        else:
            x += 1


def main():
    n = int(input())
    print(min_moves(n))


if __name__ == '__main__':
    main()
