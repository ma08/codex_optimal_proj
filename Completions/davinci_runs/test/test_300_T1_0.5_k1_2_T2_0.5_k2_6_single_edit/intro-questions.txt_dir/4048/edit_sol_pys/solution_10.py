
def min_moves(n):
    x, y = 1, 1
    moves = 0
    while n >= x * y:
        moves += 1
        if n < x * y:
            y -= 1
        else:
            x += 1


def main():
    n = int(input())
    if n == 1:
        print(0)
    else:
        print(min_moves(n))


if __name__ == '__main__':
    main()
