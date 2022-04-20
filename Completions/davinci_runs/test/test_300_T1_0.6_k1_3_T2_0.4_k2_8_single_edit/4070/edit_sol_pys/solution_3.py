

def chess_knight(n):
    return chess_knight(n // 2) + 1 if n % 2 == 0 else chess_knight(((n + 1) // 2)) + 1


if __name__ == '__main__':
    n = int(input())
    if n == 1:
        print(0)
    elif n == 2:
        print(1)
    elif n == 3:
        print(3)
    else:
        print(chess_knight(n))
