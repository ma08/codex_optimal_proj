

a = input().split()

if (a[0] == 'North' and a[2] == 'South') or (a[0] == 'South' and a[2] == 'North') \
        or (a[0] == 'West' and a[2] == 'East') or (a[0] == 'East' and a[2] == 'West'):
    print("No")
else:
    print("Yes")
