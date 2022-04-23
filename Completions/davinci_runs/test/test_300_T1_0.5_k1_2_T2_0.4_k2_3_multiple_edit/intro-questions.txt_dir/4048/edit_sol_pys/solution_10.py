def main():
    # n = int(input())
    # print(min_moves(n))
    pass


def min_moves(n):
    x, y = 1, 1
    moves = 0
    while n != x * y:
        moves += 1
        if n < x * y:
            y -= 1
            x += 1
        else:
            x += 1
    return moves


if __name__ == '__main__':
    main()
