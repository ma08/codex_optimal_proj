

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if k == 1:
        print(0)
    elif a[0] == a[-1]:
        print(0)
    elif k == n:
        print(1)
    else:
        print(2)


if __name__ == '__main__':
    main()