def min_moves(n):
    x, y = 1, 1
    moves = 0
    while True:
        moves += 1
        if n == x * y:
            return moves
        elif n < x * y:
            y -= 1
            x += 1
        else:
            x += 1


def main():
    print(min_moves(int(input())))


if __name__ == '__main__':
    main()
