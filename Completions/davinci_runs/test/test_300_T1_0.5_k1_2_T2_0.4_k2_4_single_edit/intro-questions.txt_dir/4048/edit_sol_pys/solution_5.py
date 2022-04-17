
def min_moves(n):
    x, y = 1, 1  # Start from 1x1
    moves = 0
    while True:
        moves += 1
        if n == x * y:  # Found the right number
            return moves
        elif n < x * y:  # Too big, go back to the previous row
            y -= 1
            x += 1
        else:  # Too small, go to the next row
            x += 1


def main():
    n = int(input())
    print(min_moves(n))


if __name__ == '__main__':
    main()
