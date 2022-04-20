

h1, m1 = map(int, input().split(':'))
h2, m2 = map(int, input().split(':'))

if h1 == h2:
    if m1 == m2:
        print(str(h1).zfill(2) + ':' + str(m1).zfill(2))
    else:
        print(str(h1).zfill(2) + ':' + str(int((m1 + m2) / 2)).zfill(2))
else:
    if m1 == m2:
        print(str(h1 + 1).zfill(2) + ':' + str(m1).zfill(2))
    else:
        print(str(h1 + 1).zfill(2) + ':' + str(int((m1 + m2) / 2)).zfill(2))
