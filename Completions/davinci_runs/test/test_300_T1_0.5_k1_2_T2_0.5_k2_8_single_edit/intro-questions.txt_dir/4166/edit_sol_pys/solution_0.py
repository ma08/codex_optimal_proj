N = int(input())


A = list(map(int, input().split()))

max_num = max(A)
min_num = min(A)

diff = max_num - min_num

# print(diff)

if diff == 0:
    print(0)
    exit()

print(-1)
