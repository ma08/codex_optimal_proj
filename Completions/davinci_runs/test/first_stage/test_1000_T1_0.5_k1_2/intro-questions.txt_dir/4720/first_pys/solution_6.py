

# N = Number of groups of audiences
# l = Left-most seat
# r = Right-most seat
N = int(input())
audience = [list(map(int, input().split())) for _ in range(N)]

s = set()
for l, r in audience:
    for i in range(l, r+1):
        s.add(i)

print(len(s))