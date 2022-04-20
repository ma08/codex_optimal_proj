#

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n % 2 == 0:
        if a[0] == a[-1]:
            print(0)
        else:
            print(-1)
    else:
        if a[0] == a[-1]:
            print(0)
        else:
            if a[0] + 1 == a[-1]:
                print(1)
            else:
                print(-1)

if __name__ == '__main__':
    main()
