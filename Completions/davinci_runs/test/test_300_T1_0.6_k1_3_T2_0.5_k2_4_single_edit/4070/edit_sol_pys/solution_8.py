

def chess_knight(n, m):
    if n == 1 or m == 1:
        return 1
    elif n == 2 or m == 2:
        return 2
    elif n == 3 or m == 3:
        return 4
    elif n % 2 == 0 or m % 2 == 0:
        return chess_knight(n//2, m//2) + 1
    elif n % 2 != 0 or m % 2 != 0:
        return chess_knight(((n+1)//2), ((m+1)//2)) + 1


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(chess_knight(n, m))
