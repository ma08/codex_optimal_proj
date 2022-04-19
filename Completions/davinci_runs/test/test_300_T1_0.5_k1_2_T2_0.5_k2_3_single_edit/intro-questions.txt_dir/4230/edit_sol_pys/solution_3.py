n = int(input())
p = list(map(int, input().split()))


p.sort()

print(p[int((n-1)/2)])

count = [0] * (p[n-1] + 1)

for i in range(n):
    count[p[i]] += 1

for i in range(p[n-1] + 1):
    if count[i] > 1:
        print(i)
        break




x = int(input())  # 中央値
n = int(input())  # 個数
p = list(map(int, input().split()))  # リスト

p.sort()

if x < p[0]:
    print(p[0] - x)
elif x > p[n-1]:
    print(x - p[n-1])
else:
    print(abs(x - p[int((n-1)/2)]))
