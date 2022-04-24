

def chess_knight(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 3
    else:
        return chess_knight(n//2) + chess_knight(((n+1)//2))


if __name__ == '__main__':
    print(chess_knight(int(input())))
