

def main():
    n, r = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] == 1:
            continue
        for j in range(1, r + 1):
            if i - j < 0 or i + j >= n:
                break
            if a[i - j] == 1 or a[i + j] == 1:
                a[i] = 1
                ans += 1
                break
        else:
            print(-1)
            return
    print(ans)

main()