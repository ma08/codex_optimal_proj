

a = input().split()

if (a[0] == 'North' and a[2] == 'South') or (a[0] == 'South' and a[2] == 'North') or (a[0] == 'East' and a[2] == 'West') or (a[0] == 'West' and a[2] == 'East') or (a[1] == 'North' and a[3] == 'South') or (a[1] == 'South' and a[3] == 'North') or (a[1] == 'East' and a[3] == 'West') or (a[1] == 'West' and a[3] == 'East'):
    print("No")
else:
    print("Yes")
