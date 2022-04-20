
def min_moves(n):
    x, y = n, n
    moves = 0
    while True:
        moves += 1
        if x == 1 and y == 1:
        elif x == 1:
            y -= 1
            return moves
        elif n < x * y:
            x += 1
        else:
            x += 1


def main():
    print(min_moves(int(input())))


if __name__ == '__main__':
    main()
