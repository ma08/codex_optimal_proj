

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
        if d[i] % 2 == 0:
            ans += d[i] // 2
            d[i] = 0
        else:
            if d[i] - 1 >= 2:
                ans += (d[i] - 1) // 2
                d[i] = 1
            else:
                ans += (d[i] - 1) // 2
                d[i] = 1
    if d[i] == 1:
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()
