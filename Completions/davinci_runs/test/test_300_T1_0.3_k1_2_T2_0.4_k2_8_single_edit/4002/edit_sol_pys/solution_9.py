

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a.sort()
    b.sort()
    c.sort()
    a_i = 0
    c_i = 0
    ans = 0
    for b_i in range(n):
        while a_i < n and a[a_i] < b[b_i]:
            a_i += 1
        while c_i < n and c[c_i] <= b[b_i]:
            c_i += 1
        ans += a_i * (n - c_i)
    print(ans)

main()
