

n, b, a = map(int, input().split())
s = list(map(int, input().split()))

ans = 0

# (b, a)
# b: battery
# a: accumulator

battery = b
accumulator = a

for si in s:
    if si == 1:
        if battery < b:
            battery += 1
            accumulator -= 1
        elif accumulator < a:
            accumulator += 1
        else:
            battery = b
            accumulator = a
    else:
        if battery > 0:
            battery -= 1
        elif accumulator > 0:
            accumulator -= 1
        else:
            break
    ans += 1

print(ans)