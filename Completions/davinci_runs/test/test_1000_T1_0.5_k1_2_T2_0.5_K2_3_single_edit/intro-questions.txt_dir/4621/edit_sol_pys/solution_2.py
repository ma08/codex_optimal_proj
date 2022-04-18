
s = []
H, W = map(int, input().split())

for i in range(H):
    s.append(input())
    s.append(input())
for i in range(H):
    print(s[i * 2])
    print(s[i * 2 + 1])
