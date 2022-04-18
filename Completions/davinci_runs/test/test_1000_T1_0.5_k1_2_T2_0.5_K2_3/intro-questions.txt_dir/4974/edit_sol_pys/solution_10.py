# https://codeforces.com/problemset/problem/158/A

r, n = map(int, input().split())
booked = set()
for _ in range(n):
    booked.add(input())
for i in range(1, r+1):
    if i not in booked:
        print(i)
        break
else:
    print("too late")
