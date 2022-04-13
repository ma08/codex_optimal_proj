pieces = list(map(int, input().split()))

for i in range(6):
    if i == 0:
        print(1 - pieces[i], end=' ')
    elif i == 1:
        print(1 - pieces[i], end=' ')
    elif i == 2:
        print(2 - pieces[i], end=' ')
    elif i == 3:
        print(2 - pieces[i], end=' ')
    elif i == 4:
        print(2 - pieces[i], end=' ')
    else:
        print(8 - pieces[i], end=' ')
