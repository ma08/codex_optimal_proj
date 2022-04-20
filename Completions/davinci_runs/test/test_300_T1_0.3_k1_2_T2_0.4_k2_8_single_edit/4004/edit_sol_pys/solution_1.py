

def main():
    n = int(input())
    a = list(map(int, input().split()))  # list of numbers
    # print(a)
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
            if a[0] + 1 == a[-1] or a[0] == a[-2]:
                print(1)
            else:
                print(-1)

if __name__ == '__main__':
    main()
