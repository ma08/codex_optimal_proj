

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        j = i
        while j + 1 < n and a[j] < a[j + 1]:
            j += 1
        ans = max(ans, j - i + 1)

    print(ans)

if __name__ == '__main__':
    solve()