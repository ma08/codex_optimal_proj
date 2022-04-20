

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == a[-1]:
        print(0)
    elif a[0] + 1 == a[-1]:
        if n % 2 == 0:
            print(1)
        elif n % 2 == 1:
            print(2)
    else:
        print(-1)


if __name__ == '__main__':
    main()
