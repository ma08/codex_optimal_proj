


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(0)
    s = 0
    ans = 0
    for i in range(n):
        s += a[i]
        if s == 0:
            ans += 1
            s += 1
        elif s == 1:
            ans += 1
            s -= 1
        elif s == -1:
            ans += 1
            s += 1
    print(ans)


if __name__ == '__main__':
    main()