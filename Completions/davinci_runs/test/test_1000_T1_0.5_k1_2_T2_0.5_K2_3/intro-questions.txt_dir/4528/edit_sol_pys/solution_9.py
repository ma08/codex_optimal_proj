
# --------------------------------------------------------------------------------------------------------------------------
t = int(input())
for i in range(t):
    h, m = map(int, input().split())
    print(abs(h - 12)*60 + abs(m - 60))
