

def main():
    A, B = map(int, input().split())
    if A == 1 or B == 1:
        print(A*B)
    elif A == 2:
        if B == 2 or B == 3 or B == 5 or B == 7:
            print(A*B)
        else:
            print(-1)
    elif A == 3:
        if B == 2 or B == 3 or B == 5 or B == 7:
            print(A*B)
        else:
            print(-1)
    elif A == 4:
        if B == 3 or B == 5 or B == 7:
            print(A*B)
        else:
            print(-1)
    elif A == 5:
        if B == 2 or B == 3 or B == 5 or B == 7:
            print(A*B)
        else:
            print(-1)
    elif A == 6:
        if B == 5 or B == 7:
            print(A*B)
        else:
            print(-1)
    elif A == 7:
        if B == 2 or B == 3 or B == 5 or B == 7:
            print(A*B)
        else:
            print(-1)
    elif A == 8:
        if B == 3 or B == 5 or B == 7:
            print(A*B)
        else:
            print(-1)
    elif A == 9:
        if B == 2 or B == 3 or B == 5 or B == 7:
            print(A*B)
        else:
            print(-1)
    else:
        print(-1)

if __name__ == '__main__':
    main()
