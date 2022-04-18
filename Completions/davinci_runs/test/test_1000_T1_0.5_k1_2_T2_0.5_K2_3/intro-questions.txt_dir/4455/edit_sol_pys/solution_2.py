def solve(n, skills, quarrels):
    result = []
    for i in range(n):
        temp = 0
        for j in range(n):
            if skills[i] > skills[j]:
                if [i + 1, j + 1] not in quarrels:
                    temp += 1
            if skills[i] < skills[j]:
                if [j + 1, i + 1] not in quarrels:
                    temp += 1
        result.append(temp)
    return result


print(solve(4, [1, 2, 3, 4], [[1, 2], [3, 4]]))
