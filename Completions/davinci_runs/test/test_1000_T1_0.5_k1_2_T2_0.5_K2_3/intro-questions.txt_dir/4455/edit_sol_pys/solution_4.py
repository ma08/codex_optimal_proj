def solve(n, skills, quarrels):  # n - number of students, skills - list of skills, quarrels - list of quarrels
    result = [0] * n  # list of results
    for i in range(n):  # for each student
        for j in range(i + 1, n):  # for each other student
            if skills[i] > skills[j]:  # if i's skills are better than j's
                if [i + 1, j + 1] not in quarrels:  # if they don't quarrel
                    result[i] += 1  # i is better than j
            if skills[i] < skills[j]:  # if i's skills are worse than j's
                if [j + 1, i + 1] not in quarrels:  # if they don't quarrel
                    result[i] += 1  # i is worse than j
    return result  # return result
