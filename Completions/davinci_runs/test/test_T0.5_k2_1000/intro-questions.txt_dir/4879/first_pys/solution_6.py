

a = input().split()

if (a[0] == 'North' and a[2] == 'South') or (a[0] == 'South' and a[2] == 'North'):
    print("No")
else:
    print("Yes")