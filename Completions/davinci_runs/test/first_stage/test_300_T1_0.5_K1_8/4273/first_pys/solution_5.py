

N = int(input())
names = [input() for _ in range(N)]

def solve(N, names):
    d = {}
    for name in names:
        first_letter = name[0]
        if first_letter == 'M' or first_letter == 'A' or first_letter == 'R' or first_letter == 'C' or first_letter == 'H':
            if first_letter not in d:
                d[first_letter] = 0
            d[first_letter] += 1

    cnt = 0
    for key1 in d:
        for key2 in d:
            for key3 in d:
                if key1 != key2 and key2 != key3 and key1 != key3:
                    cnt += d[key1] * d[key2] * d[key3]
    return cnt

print(solve(N, names))