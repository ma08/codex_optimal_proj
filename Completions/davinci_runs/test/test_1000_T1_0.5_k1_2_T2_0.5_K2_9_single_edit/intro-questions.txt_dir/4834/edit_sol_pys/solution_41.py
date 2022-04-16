

n = int(input().strip())
teams = [int(x) for x in input().strip().split()]

teams = sorted(teams)

total_time = 0

for i in range(n):
    total_time += teams[i] * (n - i)

print(total_time)
