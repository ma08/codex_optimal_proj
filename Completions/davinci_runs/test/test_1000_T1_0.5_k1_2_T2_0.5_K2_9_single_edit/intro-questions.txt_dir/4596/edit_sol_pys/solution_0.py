
n = int(input())
a = list(map(int, input().split()))

cnt = 0
while all(a % 2 == 0 for a in a):
    a = [a / 2 for a in a]
    cnt += 1

print(cnt)
