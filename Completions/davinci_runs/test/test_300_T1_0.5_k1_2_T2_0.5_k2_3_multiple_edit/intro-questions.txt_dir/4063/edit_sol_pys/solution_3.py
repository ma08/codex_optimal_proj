

n = int(input())
d = list(map(int, input().split()))  # 入力

d.sort(reverse=True)  # 降順ソート

cnt = 0
for i in range(n//2):
    if d[i] == d[i+n//2]:
        cnt += 1
    else:
        break


# https://atcoder.jp/contests/abc086/tasks/abc086_b

a, b = map(int, input().split())

if int(str(a)+str(b))**(1/2) % 1 == 0:
    print("Yes")
else:
    print("No")
print(n//2 + cnt)
