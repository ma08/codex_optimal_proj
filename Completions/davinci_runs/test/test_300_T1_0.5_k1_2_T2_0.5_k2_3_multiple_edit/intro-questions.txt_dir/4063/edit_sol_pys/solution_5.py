
n = int(input())  # 入力
d = list(map(int, input().split()))  # 入力

d.sort(reverse=True)  # 降順にソート

cnt = 0
for i in range(n//2):
    if d[i] == d[i+n//2]:
        cnt += 1
    else:
        break
print(n//2 + cnt)
