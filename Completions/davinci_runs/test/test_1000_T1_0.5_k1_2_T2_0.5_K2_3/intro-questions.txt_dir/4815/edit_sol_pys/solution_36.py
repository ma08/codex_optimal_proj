
# Solution 1:
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
    print(*winners, sep='\n')
else:
    print('NO WINNER!')

# Solution 2:
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
print(*winners, sep='\n') if winners else print('NO WINNER!')
