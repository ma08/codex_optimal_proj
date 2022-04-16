

S = input()

def get_min_diff(S):
    min_diff = 10000
    for i in range(len(S) - 2):
        x = int(S[i:i+3])
        diff = abs(x - 753)
        if diff < min_diff:
            min_diff = diff
    return min_diff

print(get_min_diff(S))
