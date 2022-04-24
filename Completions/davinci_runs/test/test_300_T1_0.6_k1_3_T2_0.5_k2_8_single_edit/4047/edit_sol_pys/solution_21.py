

def main():
    n = int(input())
    x = list(map(int, input().split()))
    m = min(x)
    a = [i - m for i in x]
    a.sort()
    s = sum(a)
    if s % n != 0:
        print(-1)
    else:
        s //= n
        if a[0] == a[-1]:
            print(0)
        else:
            c = 0
            for i in a:
                c += abs(i - s)
            print(c // 2)

if __name__ == '__main__':
    main()
