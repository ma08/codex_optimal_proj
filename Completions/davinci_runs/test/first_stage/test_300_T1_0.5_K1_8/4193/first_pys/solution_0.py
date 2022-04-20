

a = []
a.append(list(map(int, input().split())))
a.append(list(map(int, input().split())))
a.append(list(map(int, input().split())))
b = list(map(int, input().split()))

# search for rows
for i in range(3):
    for j in range(3):
        if a[i][j] in b:
            b.remove(a[i][j])
        else:
            break
    else:
        print('Yes')
        exit()

# search for columns
for i in range(3):
    for j in range(3):
        if a[j][i] in b:
            b.remove(a[j][i])
        else:
            break
    else:
        print('Yes')
        exit()

# search for diagonals
for i in range(3):
    if a[i][i] in b:
        b.remove(a[i][i])
    else:
        break
else:
    print('Yes')
    exit()

for i in range(3):
    if a[i][2-i] in b:
        b.remove(a[i][2-i])
    else:
        break
else:
    print('Yes')
    exit()

print('No')