

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (n-i)
    print(ans)

def main():
    k = int(input())
    x = 7
    i = 1
    while True:
        if x % k == 0:
            print(i)
            return
        x = x * 10 + 7
        i += 1

if __name__ == '__main__':
    main()
