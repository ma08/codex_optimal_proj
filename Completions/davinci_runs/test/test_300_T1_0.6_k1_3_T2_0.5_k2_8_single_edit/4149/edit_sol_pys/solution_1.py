# Задача №9. Количество пар
# https://informatics.mccme.ru/mod/statements/view3.php?id=206&chapterid=9#1

n = int(input())
b = [int(x) for x in input().split()]

a = []

for i in range(n):
    if b[i] in b[n:]:
        a.append(b[i])
    else:
        for j in range(n, 2*n):
            if b[j] == b[i]:
                a.append(b[j])
                break

print(*a)
