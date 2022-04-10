
n = int(input())
a = list(map(int, input().split()))

min_val = min(a)
max_val = max(a)
if min_val == max_val:
    print(0)
    exit()

diff = max_val - min_val
for i in range(1, diff + 1):
    if (max_val - i) % n == 0 and (min_val + i) % n == 0 and (max_val - i) // n == (min_val + i) // n:
        print(i)
        exit()
print(-1)
