def solve(n, s):
    counts = [0, 0]
    for i in range(n):
        counts[0 if s[i] == '(' else 1] += 1


    if counts[0] != counts[1]:
        return 0
    else:
        return n // 2
