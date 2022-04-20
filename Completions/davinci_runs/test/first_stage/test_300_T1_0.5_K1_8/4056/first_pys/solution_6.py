

#Solution
input()
l = [int(x) for x in input().split()]
min_num = min(l)

ans = []
for i in range(1, min_num+1):
    if all(x % i == 0 for x in l):
        ans.append(i)

print(len(ans))