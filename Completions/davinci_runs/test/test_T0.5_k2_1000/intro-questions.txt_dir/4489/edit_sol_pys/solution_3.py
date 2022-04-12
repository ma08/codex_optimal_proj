

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    m = int(input())
    t = [input() for _ in range(m)]

    ans = 0
    for si in s:
        ans += 1 if si not in t else -1

    print(ans)

if __name__ == '__main__':
    main()
