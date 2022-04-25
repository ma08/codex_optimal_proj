def min_moves(n):
    moves = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
        moves += 1
    return moves


# def min_moves(n):
#     x, y = 1, 1
#     moves = 0
#     while True:
#         moves += 1
#         if n == x * y:
#             return moves
#         elif n < x * y:
#             y -= 1
#             x += 1
#         else:
#             x += 1


def main():
    n = int(input().strip())
    print(min_moves(n), end="")


if __name__ == '__main__':
    main()
