# N = Number of groups of audiences
# l = Leftmost seat
# r = Rightmost seat
N = int(input())
audience = [list(map(int, input().split())) for _ in range(N)]

s = set()
for l, r in audience:
    for i in range(l, r+1):
        s.add(i)

print(len(s))

# N = Number of groups of audiences
# l = Leftmost seat
# r = Rightmost seat
N = int(input())
audience = [list(map(int, input().split())) for _ in range(N)]

s = set()
for l, r in audience:
    for i in range(l, r+1):
        s.add(i)

print(len(s))
