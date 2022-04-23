

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a.sort()
    b.sort()
    c.sort()
    i = j = k = 0
    ans = 0
    while i < n and j < n and k < n:
        if a[i] < b[j] < c[k]:
            ans += 1
            i += 1
            j += 1
            k += 1
        elif a[i] < b[j]:
            i += 1
        elif b[j] < c[k]:
            j += 1
        else:
            k += 1
    print(ans)

main()
