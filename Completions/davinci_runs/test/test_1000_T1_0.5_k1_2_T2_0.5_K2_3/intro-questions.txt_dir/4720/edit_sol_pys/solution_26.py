

# N = Number of groups of audiences, l = Leftmost seat, r = Rightmost seat
N, l, r = map(int, input().split())
audience = [list(map(int, input().split())) for _ in range(N)]  # N groups of audience

s = set()
for l, r in audience:
    for i in range(l, r+1):
        s.add(i)

print(len(s))
