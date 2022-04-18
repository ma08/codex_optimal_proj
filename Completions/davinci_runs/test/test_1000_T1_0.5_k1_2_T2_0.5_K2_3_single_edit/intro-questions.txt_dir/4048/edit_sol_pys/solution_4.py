
def min_moves(n):
    x, y = 1, 1  # x = width, y = height
    moves = 0
    while True:
        moves += 1
        if n == x * y:  # if x*y = n
            return moves
        elif n < x * y:  # if x*y > n
            y -= 1
            x += 1
        else:  # if x*y < n
            x += 1


def main():
    n = int(input())  # n = number of squares
    print(min_moves(n))


if __name__ == '__main__':
    main()
