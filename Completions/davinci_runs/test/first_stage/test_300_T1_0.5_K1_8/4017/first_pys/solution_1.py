

def solve(a):
    n = len(a)
    s = sum(a)
    ans = []
    for i in range(n):
        if a[i] == s - a[i]:
            ans.append(i + 1)
    return ans

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    ans = solve(a)
    print(len(ans))
    if len(ans) > 0:
        print(*ans)