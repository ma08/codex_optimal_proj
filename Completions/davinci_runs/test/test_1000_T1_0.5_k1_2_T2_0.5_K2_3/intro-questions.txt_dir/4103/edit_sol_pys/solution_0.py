

def main():
    n, b, a = map(int, input().split())
    s = list(map(int, input().split()))
    ans = 0
    i = 0
    while i < n:
        if s[i] == 1:
            if a < b:  # aがbより少ない時
                a += 1
            else:
                b += 1
        if a > 0:  # aがある時
            a -= 1
            ans += 1
        elif b > 0:  # bがある時
            b -= 1
            ans += 1
        else:
            break
        i += 1
    print(ans)


if __name__ == "__main__":
    main()
