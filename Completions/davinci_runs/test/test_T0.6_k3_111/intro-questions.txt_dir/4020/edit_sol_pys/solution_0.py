
h1, m1 = map(int, input().split(':'))
h2, m2 = map(int, input().split(':'))

if m2 < m1:
    m2 += 60
    h2 -= 1
if h2 < h1:
    h2 += 24

tot_min = (h2 - h1) * 60 + m2 - m1
mid_min = tot_min // 2
h3 = h1 + mid_min // 60
m3 = m1 + mid_min % 60
if m3 >= 60:
    m3 -= 60
    h3 += 1
if h3 >= 24:
    h3 -= 24

print('{:02d}:{:02d}'.format(h3, m3))
