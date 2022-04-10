

def main():
    n, r = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    i = 0
    while i < n:
        if a[i] == 0:
            j = i + 1
            while j < n and a[j] == 0:
                j += 1
            if j == n:
                ans = -1
                break
            ans += 1
            i = j + r - 1
        else:
            i += r
    print(ans)

main()