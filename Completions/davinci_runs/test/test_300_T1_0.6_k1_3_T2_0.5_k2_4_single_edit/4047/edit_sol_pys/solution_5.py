

def main():
    n = int(input())
    x = list(map(int, input().split()))
    m = min(x)
    y = [i - m for i in x]
    y.sort()
    s = sum(y)
    if s % n != 0:
        print(-1)
    else:
        s //= n
        if y[0] == y[-1]:
            print(0)
        else:
            c = 0
            for i in y:
                c += abs(i - s)
            print(c//2)

if __name__ == '__main__':
    main()
