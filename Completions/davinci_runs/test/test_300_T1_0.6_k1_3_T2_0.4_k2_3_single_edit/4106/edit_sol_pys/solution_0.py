

def main():
    n, k, x = map(int,input().split())
    a = list(map(int,input().split()))
    res = 0
    for i in range(n):
        res += a[i]
    for i in range(k):
        res += x
    for i in range(n-k):
        res -= a[i]
    print(res)

if __name__ == '__main__':
    main()
