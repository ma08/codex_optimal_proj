
#-----main-----

h1, m1 = map(int, input().split(':'))
h2, m2 = map(int, input().split(':'))

if m1 == m2:
    h3, m3 = h1, m1
elif m1 < m2:
    h3, m3 = h1, (m1 + m2) // 2
else:
    h3, m3 = h1 + 1, (m1 + m2) // 2

print('{:02d}:{:02d}'.format(h3, m3))
