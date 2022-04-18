

def chess_knight(n):
    if n == 1 or n == 2 or n == 3:
        return n
    else:
        if n % 2 == 0:
            return chess_knight(n//2) + 1
        else:
            return chess_knight(((n+1)//2)) + 1


if __name__ == '__main__':
    print(chess_knight(int(input())))
