

#SOLUTION

def solve(n, a):
    if n == 1:
        return "YES\n" + str(a[0])
    if n % 2 == 0:
        return "NO"
    m = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            m[i][j] = a[i * n + j]
    for i in range(n):
        for j in range(n):
            if m[i][j] != m[n - 1 - i][n - 1 - j] or m[i][j] != m[j][i]:
                return "NO"
    return "YES\n" + "\n".join(map(lambda x: " ".join(map(str, x)), m))

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))