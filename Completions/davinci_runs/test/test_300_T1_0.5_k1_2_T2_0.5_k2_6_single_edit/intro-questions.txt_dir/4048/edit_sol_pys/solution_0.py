
def min_moves(n):
    x, y = 1, 0
    if n == 1:
        return 0
    moves = 0
    while True:
        y += 1
        moves += 1
        if n == x * y:
            return moves
        elif n < x * y:
            y -= 2
            x += 1
        else:
            x += 1

def main():
    n = int(input())
    print(min_moves(n))

if __name__ == '__main__':
    main()
