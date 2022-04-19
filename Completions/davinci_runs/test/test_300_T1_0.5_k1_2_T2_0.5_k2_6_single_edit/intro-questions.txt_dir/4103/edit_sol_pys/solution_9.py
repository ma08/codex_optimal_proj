

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    a.sort()
    b.sort()
    c.sort()

    ans = 0
    for i in range(n):
        x = b[i]
        a_idx = a.index(x)
        c_idx = c.index(x)
        ans += a_idx * (n - c_idx)

    print(ans)

if __name__ == "__main__":
    main()
