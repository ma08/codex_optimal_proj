
import sys
sys.setrecursionlimit(10 ** 6)
n, b, a = map(int, input().split())
s = list(map(int, input().split()))

def rec(current_battery, current_accumulator, segments_count, i):
    if i == n:
        return segments_count
    if current_accumulator >= 1:
        current_accumulator -= 1
    else:
        current_battery -= 1
    if s[i] == 1:
        if current_battery < b:
            current_battery += 1
        else:
            current_accumulator += 1
    segments_count += 1
    if current_battery == 0 and current_accumulator == 0:
        return segments_count
    return max(rec(current_battery, current_accumulator, segments_count, i + 1), segments_count)

print(rec(b, a, 0, 0))
