

n, b, a = map(int, input().split())
s = list(map(int, input().split()))

def solve(n, b, a, s):
    max_segments = 0
    current_battery = b
    current_accumulator = a
    for i in range(n):
        if current_accumulator >= 1:
            current_accumulator -= 1
        else:
            current_battery -= 1
        if s[i] == 1 and current_battery < b:
            current_battery += 1
        elif s[i] == 1:
            current_accumulator += 1
        max_segments += 1
        if current_battery == 0 and current_accumulator == 0:
            break
    return max_segments

print(solve(n, b, a, s))
