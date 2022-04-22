

def main():
    a, b = map(int, input().split())
    if a == 1:
        print(a*b)
    elif a == 2 and (b == 2 or b == 3 or b == 5 or b == 6):
        print(a*b)
    elif a == 3 and (b == 2 or b == 3 or b == 5 or b == 6):
        print(a*b)
    elif a == 4 and (b == 3 or b == 5 or b == 7):
        print(a*b)
    elif a == 5 and (b == 2 or b == 3 or b == 5 or b == 6):
        print(a*b)
    elif a == 6 and (b == 5 or b == 7):
        print(a*b)
    elif a == 7 and (b == 2 or b == 3 or b == 5 or b == 6):
        print(a*b)
    elif a == 8 and (b == 3 or b == 5 or b == 7):
        print(a*b)
    elif a == 9 and (b == 2 or b == 3 or b == 5 or b == 6):
        print(a*b)
    else:
        print(-1)

if __name__ == '__main__':
    main()
