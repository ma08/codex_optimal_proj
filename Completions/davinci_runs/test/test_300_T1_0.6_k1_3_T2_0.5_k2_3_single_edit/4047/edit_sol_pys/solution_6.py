

def main():
    n = int(input())
    x = list(map(int, input().split()))
    m = min(x)
    x = [i - m for i in x]  # make all elements positive
    x.sort()
    if x[0] == x[-1]:
        print(0)
    else:  # x[0] != x[-1]
        s = sum(x)
        if s % n:
            print(-1)
        else:
            s //= n
            c = 0
            for i in x:
                c += abs(i - s)
            print(c // 2)

if __name__ == '__main__':
    main()
