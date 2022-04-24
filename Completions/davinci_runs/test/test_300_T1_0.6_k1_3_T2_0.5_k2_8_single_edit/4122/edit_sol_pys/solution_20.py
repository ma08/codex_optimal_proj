

# Write your code here
n, m = [int(x) for x in input().split()]
d = [int(x) for x in input().split()] + [0]

hp = n
for i in range(m):
    hp -= d[i]
    if hp < 0:
        print(i)
        break
else:
    print(-1)
