

N = int(input())
sour = 1
bit = 0
for i in range(N):
    S, B = map(int, input().split())
    sour *= S
    bit += B
print(abs(sour-bit))

print(abs(sourness-bitterness))
