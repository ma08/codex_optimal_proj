

# Write your code here
h, n = [int(x) for x in input().split()]  # input h and n
d = [int(x) for x in input().split()]  # input damage

hp = h  # hp is h
for i in range(n):
    hp += d[i]  # hp = hp + damage
    if hp <= 0:  # if hp is less than 0
        print(i+1)  # print i+1
        break
else:
    print(-1)
