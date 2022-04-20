
#-----main-----

h1, m1 = map(int, input().split(':'))
h2, m2 = map(int, input().split(':'))

h3 = h1
m3 = (m1 + m2) // 2

if m3 >= 60:
    h3 += 1
    m3 -= 60

print('{:02d}:{:02d}'.format(h3, m3))
