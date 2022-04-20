

def check_acceptable(a, k):
    n = len(a)
    m = len(a[0])
    s = []
    for j in range(m):
        for i in range(n):
            s.append(a[i][j])
    for i in range(len(s) - 1):
        if abs(s[i] - s[i + 1]) < k:
            return False
    return True

def find_max_acceptable(a):
    n = len(a)
    m = len(a[0])
    max_k = 0
    for i in range(n):
        for j in range(i + 1, n):
            a[i], a[j] = a[j], a[i]
            for k in range(max_k, min(a[i]) - max(a[j]), -1):
                if check_acceptable(a, k):
                    max_k = k
                    break
            a[i], a[j] = a[j], a[i]
    return max_k

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
print(find_max_acceptable(a))