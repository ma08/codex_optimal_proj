n = int(input())
seats = [0] * 100000
for i in range(n):
    l, r = map(int, input().split())
    for j in range(l, r + 1):
        seats[j - 1] = 1
print(sum(seats))
