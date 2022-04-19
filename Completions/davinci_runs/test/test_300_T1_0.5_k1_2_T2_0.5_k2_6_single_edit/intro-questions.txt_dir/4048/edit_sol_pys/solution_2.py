
def min_moves(n):
    x, y = 2, 2
    moves = 0
    while True:
        moves += 1
        if n <= x * y:
            return moves
        elif n % x == 0:
            y = n // x
        else:
            x = n // y + 1

def main():
    n = int(input().strip())
    print(min_moves(n))


if __name__ == '__main__':
    main()
