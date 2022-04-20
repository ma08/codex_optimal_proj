

N = int(input())
p = list(map(int, input().split()))

p_sorted = sorted(p)

for i in range(N):
    if p[i] == p_sorted[i]:
        continue
    else:
        p[i], p[p.index(p_sorted[i])] = p[p.index(p_sorted[i])], p[i]
        if p == p_sorted:
            print("YES")
            exit()



N = int(input())
p = list(map(int, input().split()))

p_sorted = sorted(p)

for i in range(N):
    if p[i] == p_sorted[i]:
        continue
    else:
        p[i], p[p.index(p_sorted[i])] = p[p.index(p_sorted[i])], p[i]
        if p == p_sorted:
            print("YES")
            exit()

print("NO")
print("NO")
