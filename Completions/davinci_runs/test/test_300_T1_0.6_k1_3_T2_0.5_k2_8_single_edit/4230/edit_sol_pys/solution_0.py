

def main():
    x, n = map(int, input().strip().split())
    if n == 0:
        print(x)
        return
    p = sorted(list(map(int, input().split())))

    for i in range(n+1):
        if i == 0:
            if x < p[i]:
                print(min(p[i]-x, x-p[i-1]))
                return
        elif i == n:
            if x > p[i-1]:
                print(min(x-p[i-1], p[i]-x))
                return
        else:
            if p[i-1] < x < p[i]:
                print(min(x-p[i-1], p[i]-x))
                return

if __name__ == '__main__':
    main()
