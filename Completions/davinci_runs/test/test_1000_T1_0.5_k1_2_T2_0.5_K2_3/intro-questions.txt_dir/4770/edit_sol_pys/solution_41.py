
n, m = map(int, input().split())

if m >= n:
    print("Dr. Chaz will have {} piece{} of chicken left over!".format(m-n, "" if m-n == 1 else "s "))
else:
    print("Dr. Chaz needs {} more piece{} of chicken!".format(n-m, "" if n-m == 1 else "s "))
