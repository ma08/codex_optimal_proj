
n, k = map(int, input().split())
skills = list(map(int, input().split()))
quarrels = []
for i in range(k):
    quarrels.append(list(map(int, input().split())) - 1)

mentors = [1] * n
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if skills[i] > skills[j]:
            if [i, j] not in quarrels and [j, i] not in quarrels:
                mentors[i] += 1
        if skills[i] < skills[j]:
            if [i, j] not in quarrels and [j, i] not in quarrels:
                mentors[j] += 1

print(*mentors)
