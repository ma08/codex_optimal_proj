
n, m = map(int, input().split())

if m >= n:
    print("Dr. Chaz will have {0} piece{1} of chicken left over!".format(m-n, "" if m-n == 1 else "s"))
else:
    print("Dr. Chaz needs {0} more piece{1} of chicken!".format(n-m, "" if n-m == 1 else "s"))
