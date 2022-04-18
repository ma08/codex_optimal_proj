
def solve(n, skills, quarrels):
    result = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if skills[i] > skills[j]:
                if [i + 1, j + 1] not in quarrels:
                    result[i] += 1
            if skills[i] < skills[j]:
                if [j + 1, i + 1] not in quarrels:
                    result[i] += 1
    return result

print(solve(3, [1, 2, 3], [[1, 2], [2, 3]]))
