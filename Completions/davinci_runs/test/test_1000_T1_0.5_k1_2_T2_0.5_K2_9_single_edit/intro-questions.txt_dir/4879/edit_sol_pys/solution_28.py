

a = input().split()

if (a[0] == 'North' and a[2] == 'South') or (a[0] == 'South' and a[2] == 'North') or (a[1] == 'North' and a[3] == 'South') or (a[1] == 'South' and a[3] == 'North'):
    print("No")
else:
    print("Yes")
