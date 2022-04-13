
n, k = map(int, input().split())
skills = list(map(int, input().split()))
quarrels = [] # список возможных споров
for i in range(k):
    quarrels.append(list(map(int, input().split())))

mentors = [0] * n # список количества возможных наставников у каждого ученика
for i in range(n):
    for j in range(i+1, n):
        if skills[i] > skills[j]:
            if [i+1, j+1] not in quarrels:
                mentors[i] += 1 # добавляем ученика в список наставников
        if skills[i] < skills[j]:
            if [j+1, i+1] not in quarrels:
                mentors[i] += 1

print(*mentors)
