

n = int(input())
a = list(map(int, input().split()))

min_a = min(a)
max_a = max(a)

if len(set(a)) == 1:
    print(0)
elif max_a - min_a < 3:
    print(-1)
else:
    print(max_a - min_a - 2)