n, m = map(int, input().split())


a = []
for _ in range(n):
    a.append(list(input()))

b = []
for _ in range(n):
    b.append(list(input()))

def check(a, b):
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return False
    return True

print(count)
