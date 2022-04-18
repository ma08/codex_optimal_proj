# https://codeforces.com/problemset/problem/158/A

r, n = map(int, input().split())
booked = set(map(int, input().split()))
for i in range(1, r + 1):
    if i not in booked: break
print(i if i <= r else "too late")
