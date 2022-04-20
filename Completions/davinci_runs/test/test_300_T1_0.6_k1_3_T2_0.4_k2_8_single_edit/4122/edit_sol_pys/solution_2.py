

# Write your code here
h, n = map(int, input().split())
d = list(map(int, input().split()))

hp = h
for i in range(n):
    hp += d[i]
    if hp <= 0:
        print(i+1)
        break
else:
    print(-1)
