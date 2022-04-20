

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [0] * n
    for i in range(n):
        c[i] = a[i] + b[i]
    c.sort()
    ans = 0
    for i in range(n):
        if c[i] == 0:
            ans += 1
        else:
            break
    for i in range(n - 1, -1, -1):
        if c[i] == 0:
            ans += 1
        else:
            break
    print(ans)

if __name__ == "__main__":
    main()
