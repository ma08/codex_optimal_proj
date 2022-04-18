
def main():
    n = int(input())
    s = [input() for _ in range(n)]
    m = int(input())
    t = [input() for _ in range(m)]

    ans = 0
    for si in s:
        if si in t:
            ans -= 1
        else:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
