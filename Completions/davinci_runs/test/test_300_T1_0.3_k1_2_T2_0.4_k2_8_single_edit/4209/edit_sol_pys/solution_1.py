

def main():
    n = int(input())
    s = sum(map(int, input().split()))
    if s % n != 0:
        print(1)
        print(1, n)
        return
    s //= n
    l = r = 0
    k = 0
    while r < n:
        if sum(map(int, input().split())) == s:
            k += 1
            print(l + 1, r + 1)
            l = r + 1
        r += 1
    if l < n:
        k += 1
        print(l + 1, n)
    print(k)

if __name__ == '__main__':
    main()
