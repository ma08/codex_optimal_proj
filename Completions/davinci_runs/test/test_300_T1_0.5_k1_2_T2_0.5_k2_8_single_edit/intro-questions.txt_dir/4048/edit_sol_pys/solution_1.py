
def min_moves(n):
    x, y = 1, 1
    moves = 0
    while n > x * y:
        moves += 1
        if n < x * y:
            x -= 1
        y += 1
    return moves


def main():
    n = int(input())
    print(min_moves(n)


if __name__ == '__main__':
    main()
