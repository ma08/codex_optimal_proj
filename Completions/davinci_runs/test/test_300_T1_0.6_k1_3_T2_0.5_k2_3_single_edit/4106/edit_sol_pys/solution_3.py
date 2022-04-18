

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    res = -1
    for i in range(n):
        if res < sum(a[i: i + x]):
            res = sum(a[i: i + x])
    print(res)

if __name__ == '__main__':
    main()
