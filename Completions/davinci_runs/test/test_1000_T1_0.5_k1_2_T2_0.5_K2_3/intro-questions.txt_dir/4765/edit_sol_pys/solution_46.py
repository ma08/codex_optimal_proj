
N = int(input())

sourness = bitterness = 0
for i in range(N):
    s, b = map(int, input().split())
    sourness += s
    bitterness += b

print(abs(sourness-bitterness))
