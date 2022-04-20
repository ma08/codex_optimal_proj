


def chess_knight(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 3
    elif n % 2 == 0:
        return chess_knight(n//2) + 1
    elif n % 2 != 0:
        return chess_knight(((n+1)//2)) + 1


if __name__ == '__main__':
    print(chess_knight(int(input())))
