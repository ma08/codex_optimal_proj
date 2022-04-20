

n = int(input())
weights = list(map(int, input().split()))

def min_diff(weights):
    min_diff = sum(weights)
    for i in range(1, len(weights)):
        s1 = sum(weights[:i])
        s2 = sum(weights[i:])
        abs_diff = abs(s1 - s2)
        if abs_diff < min_diff:
            min_diff = abs_diff
    return min_diff

print(min_diff(weights))