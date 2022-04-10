

n, b, a = map(int, input().split())
s = list(map(int, input().split()))

battery = b
accumulator = a

segments = 0

for i in range(n):
    if s[i] == 1:
        if battery < b:
            battery += 1
        else:
            accumulator += 1
    if battery > 0:
        battery -= 1
        segments += 1
    elif accumulator > 0:
        accumulator -= 1
        segments += 1
    else:
        break

print(segments)