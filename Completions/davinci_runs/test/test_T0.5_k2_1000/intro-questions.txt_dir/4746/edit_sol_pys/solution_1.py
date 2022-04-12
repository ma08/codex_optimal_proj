

# n: number of people
# m: number of pairs of people
# p: number of people that are friends
n, m = [int(x) for x in input().split()]
p = 0

for i in range(m):
    x, y = [int(x) for x in input().split()]
    if x == 1 or y == 1:
        p += 1

print(p)
