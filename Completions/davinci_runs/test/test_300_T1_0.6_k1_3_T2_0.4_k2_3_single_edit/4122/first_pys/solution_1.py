

# Write your code here
h, n = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]

hp = h
for i in range(n):
    hp += d[i]
    if hp <= 0:
        print(i+1)
        break
else:
    print(-1)