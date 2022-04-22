

def main():
    a, b = map(int, input().split())
    if a == 1 or b == 1 or a == b:
        print(a*b)
    else:
        if a % 3 == 0 or b % 3 == 0:
            print(a*b//3)
        elif (a+b) % 3 == 0:
            print(a*b//3)
        else:
            print(-1)

if __name__ == '__main__':
    main()
