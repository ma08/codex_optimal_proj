

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    i, j = 0, n - 1
    ans = 0
    while i <= j:
        if a[i] <= k:
            i += 1
            ans += 1
        elif a[j] <= k:
            j -= 1
            ans += 1
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()
