

q = int(input())
for _ in range(q):
    s = input()
    m = int(input())
    b = list(map(int, input().split()))
    res = ""
    for i in range(m):
        # find the minimum distance in b[i:]
        min_idx = min(range(i, m), key=lambda x: b[x])
        res += s[min_idx]
        s = s[:min_idx] + s[min_idx+1:]
    print(res)