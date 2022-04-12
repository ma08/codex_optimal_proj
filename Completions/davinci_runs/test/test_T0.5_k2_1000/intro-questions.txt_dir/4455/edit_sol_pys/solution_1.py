n, k = map(int, input().split())
skills = list(map(int, input().split()))
quarrels = []
for i in range(k):
    quarrels.append(list(map(int, input().split())))

mentors = [0] * n
for i in range(n):
    for j in range(n):
        if skills[i] > skills[j] and [i+1, j+1] not in quarrels and i != j:
            mentors[j] += 1

print(*mentors)
