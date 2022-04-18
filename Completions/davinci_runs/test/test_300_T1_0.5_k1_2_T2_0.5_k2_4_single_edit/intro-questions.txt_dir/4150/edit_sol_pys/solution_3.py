
n, k = map(int, input().split())
a = list(map(int, input().split()))

a = [0] + a
a.append(n + 1)  # 左右に1ずつ余裕を持たせる

# print(a)

a.sort()
# print(ans)
ans = [0] * (n + 2)

for i in range(1, n + 2):
    left = a[i - 1] + k  # 左端
    right = a[i] - k - 1  # 右端
    # print(left, right)
    if left <= right:
        ans[left] += 1  # 左端が範囲内なら+1
        ans[right + 1] -= 1

for i in range(1, n + 1):
    ans[i] += ans[i - 1]  # 累積和

ans = ans[1:]  # 左端は0なので消す

print(''.join(map(str, ans)))
