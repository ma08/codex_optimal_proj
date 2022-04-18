

def main():
    a, b = map(int, input().split())
    if a == 1 or b == 1:
        print(a*b)
    else:
        if b == 2 or b == 3 or b == 5 or b == 7 or b == 11:
            if a == 2 or a == 3 or a == 5 or a == 7 or a == 11:
                print(a*b)
            else:
                print(-1)
        elif b == 3 or b == 5 or b == 7 or b == 11:
            if a == 2 or a == 4 or a == 6 or a == 8 or a == 10:
                print(a*b)
            else:
                print(-1)
        elif b == 2 or b == 4 or b == 6 or b == 8 or b == 10:
            if a == 3 or a == 5 or a == 7 or a == 11:
                print(a*b)
            else:
                print(-1)
        else: print(-1)

if __name__ == '__main__':
    main()
