

n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    ans += a[i]

print(ans)

# --------------------------------------

s = input()
t = input()

if s == t:
    print("Yes")
    exit()

for i in range(len(s)):
    s = s[-1] + s[:-1]
    if s == t:
        print("Yes")
        exit()

print("No")

# --------------------------------------

n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    ans += a[i]

print(ans)

# --------------------------------------

s = input()
t = input()

if s == t:
    print("Yes")
    exit()

for i in range(len(s)):
    s = s[-1] + s[:-1]
    if s == t:
        print("Yes")
        exit()

print("No")
