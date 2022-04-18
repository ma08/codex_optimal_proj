n, k = map(int, input().split())
skills = list(map(int, input().split()))
quarrels = []
for i in range(k):
    quarrels.append(list(map(int, input().split())))

mentors = [0] * n
for i in range(n):
    for j in range(i+1, n):
        if skills[i] > skills[j]:
            if [i, j] not in quarrels:
                mentors[i] += 1
        if skills[i] < skills[j]:
            if [j, i] not in quarrels:
                mentors[i] += 1

print(*mentors)
