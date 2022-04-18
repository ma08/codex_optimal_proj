

def min_moves(n):
    x, y = 1, n
    moves = 0
    while True:
        moves += 1
        if x * y == n:
            break
        elif x * y > n:
            y -= 1
            x += 1
        else:
            x += 1


def main():
    n = int(input())
    print(min_moves(n) + 1)


if __name__ == '__main__':
    main()
