

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    if n == 1:
        print(0)
        return
    if n == 2:
        print(0)
        return
    if n == 3:
        if a[1] - a[0] == a[2] - a[1]:
            print(0)
        else:
            print(-1)
        return
    d = a[1] - a[0]
    c = 0
    for i in range(n - 1):
        if a[i + 1] - a[i] != d:
            c += 1
            if c > 1:
                print(-1)
                return
            if a[i + 1] - a[i] == d + 1:
                a[i] += 1
            elif a[i + 1] - a[i] == d - 1:
                a[i + 1] += 1
            else:
                print(-1)
                return
    print(c)

if __name__ == '__main__':
    main()