

# submitted
n, m, d = map(int, input().split())
c = list(map(int, input().split()))

def get_river(n, m, d, c):
    river = [0] * n
    c = [0] + c
    total = sum(c)
    if total < n or d >= n:
        return None
    for i in range(m):
        i = 0
        while c[i+1] > 0:
            river[i] = i+1
            c[i+1] -= 1
            i += 1
        if i == n:
            break
        i = n-1
        while c[i] > 0:
            river[i] = i+1
            c[i] -= 1
            i -= 1
        if i == 0:
            break
    return river if sum(river) == total else None

print("YES")
river = get_river(n, m, d, c)
if river:
    print(*river)
else:
    print("NO")
