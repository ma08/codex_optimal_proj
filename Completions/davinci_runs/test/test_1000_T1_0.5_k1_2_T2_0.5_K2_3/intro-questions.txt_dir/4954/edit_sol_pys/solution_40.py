def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a.sort()
    b.sort()
    c.sort()
    j = 0
    k = 0
    ans = 0
    for i in range(n):
        while j < n and b[j] < a[i]:
            j += 1
        while k < n and c[k] < b[j]:
            k += 1
        ans += j*k
    print(ans)


# main
main()
