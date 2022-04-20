

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    ans = 0
    for i in d:
        ans += d[i] * (d[i]-1) // 2
    for i in a:
        print(ans - d[i] + 1)

if __name__ == '__main__':
    main()
