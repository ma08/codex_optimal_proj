

n = int(input())
a = list(map(int, input().split()))

mini = min(a)
maxi = max(a)

for i in range(n):
    if a[i] == mini:
        if mini == maxi:
            print(0)
            exit()
        else:
            print(maxi - mini)
            exit()
    elif a[i] == maxi:
        print(maxi - mini)
        exit()
    else:
        if a[i] - mini > maxi - a[i]:
            print(a[i] - mini)
            exit()
        else:
            print(maxi - a[i])
            exit()