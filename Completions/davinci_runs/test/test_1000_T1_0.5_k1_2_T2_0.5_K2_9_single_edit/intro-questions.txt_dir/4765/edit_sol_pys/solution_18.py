

N = int(input())

sourness = 1
bitterness = 0
for i in range(N):
    S, B = map(int, input().split())
    sourness *= S
    bitterness += B






print(abs(sourness-bitterness))
