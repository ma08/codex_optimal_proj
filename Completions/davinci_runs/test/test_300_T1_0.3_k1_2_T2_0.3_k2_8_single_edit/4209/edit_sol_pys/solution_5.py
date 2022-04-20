

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a) // n
    l = 0
    r = 0
    k = 0
    while r < n:
        if a[r] != s:
            k += 1
            print(l + 1, r)
            l = r
        r += 1
    if l < n:
        print(1)
        print(l + 1, n)
    print(k)

if __name__ == '__main__':
    main()
