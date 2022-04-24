

def chess_knight(n):
    if n <= 3:
        return n - 1
    elif n % 2 == 1:
        return chess_knight((n + 1) // 2)
    else:
        return chess_knight(n // 2)


if __name__ == '__main__':
    print(chess_knight(int(input())))
