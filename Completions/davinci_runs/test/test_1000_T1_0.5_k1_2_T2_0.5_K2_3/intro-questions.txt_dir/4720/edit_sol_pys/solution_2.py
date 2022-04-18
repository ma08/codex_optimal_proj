# https://atcoder.jp/contests/abc085/tasks/abc085_b

# N = Number of groups of audiences
# l = Left-most seat of a group
# r = Right-most seat of a group
N = int(input())
audience = [list(map(int, input().split())) for _ in range(N)]

s = set()  # A set of seats occupied by audiences
for l, r in audience:
    for i in range(l, r+1):
        s.add(i)

print(len(s))
