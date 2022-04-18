def min_moves(n):
    x = 1
    y = 1
    moves = 0
    while True:
        moves += 1
        if n == x * y:
            return moves
        if n < x * y:
            y -= 1
            x += 1
        if n > x * y:
            x += 1


def main():
    n = int(input("Enter a number: "))
    print(min_moves(n))


if __name__ == '__main__':
    main()
