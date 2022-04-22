
#

def min_moves(n):
    x, y = 1, n
    moves = 0
    while x * y != n:
        moves += 1
        if n < x * y:
            x += 1
        else:
            y -= 1
    return moves


def main():
    n = int(input()) # number of test cases
    for i in range(n):
        print(min_moves(int(input())))


if __name__ == '__main__':
    main()
