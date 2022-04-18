

def chess_knight(n):
    return chess_knight(n//2) + 1 if n % 2 == 0 else chess_knight(((n+1)//2)) + 1


if __name__ == '__main__':
    print(chess_knight(int(input())))
