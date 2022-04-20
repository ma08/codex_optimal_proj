

def main():
    n, r = map(int, input().split())
    a = list(map(int, input().split()))

    if n == 0:
        print(-1)
        return

    if r == 0:
        if sum(a) == 0:
            print(-1)
        else:
            print(0)
        return

    ans = 0
    pos = 0
    while pos < n:
        if a[pos] == 1:
            pos += r
            ans += 1
            continue
        else:
            # try to find the closest heater
            i = pos + 1
            while i < n:
                if a[i] == 1:
                    break
                i += 1
            if i == n:
                print(-1)
                return

            # turn on the heater at position pos
            pos = i + r
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()