

# Write your code here
h, n = [int(x) for x in input().split()]  # h = 체력, n = 공격 횟수
d = [int(x) for x in input().split()]  # d = 공격력

hp = h
for i in range(n):
    hp += d[i]
    if hp <= 0:
        print(i+1)
        break
else:
    print(-1)
