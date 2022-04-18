
N = int(input())
seats = [0] * 1001

for _ in range(N):
    l, r = map(int, input().split())
    for i in range(l, r + 1):
        seats[i] += 1

print(sum(seats))
