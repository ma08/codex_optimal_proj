

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    m = int(input())
    t = [input() for _ in range(m)]

    ans = n
    for i in range(n):
        if s[i] in t:
            ans -= 1
    print(ans)

    print(ans)

if __name__ == '__main__':
    main()
