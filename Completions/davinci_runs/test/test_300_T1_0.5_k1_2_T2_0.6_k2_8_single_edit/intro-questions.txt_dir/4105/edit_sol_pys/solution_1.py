

def count(n, k, a):
    for i in range(n):
        for j in range(n):
            if a[i][j] == 0:
                return "NO"
            else:
                return "YES"

n, k = map(int, input().split())
a = [[0]*n]*n
print(count(n, k, a))
