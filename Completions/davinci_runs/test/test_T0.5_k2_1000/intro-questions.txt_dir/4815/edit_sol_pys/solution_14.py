
# Solution 1 (long)
n, p, m = map(int, input().split())
names = [input() for _ in range(n)]
winners = []
for _ in range(m):
    name, points = input().split()
    points = int(points)
    if name in names:
        p -= points
        if p <= 0:
            winners.append(name)
            p = 10
if winners:
    print('\n'.join(winners))
else:
    print('No winner!')

# Solution 2 (short)
n, p, m = map(int, input().split())
names = [input() for _ in range(n)]
winners = []
for _ in range(m):
    name, points = input().split()
    points = int(points)
    if name in names:
        p -= points
        if p <= 0:
            winners.append(name)
            p = 10
print('\n'.join(winners)) if winners else print('No winner!')
