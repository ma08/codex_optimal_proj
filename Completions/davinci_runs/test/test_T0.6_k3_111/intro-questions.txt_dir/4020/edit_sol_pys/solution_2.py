
h1, m1 = map(int, input().split(':'))
h2, m2 = map(int, input().split(':'))

m_diff = (m2 - m1) / 2

h_diff = (h2 - h1) / 2
if m_diff >= 30:
    h_diff += 0.5

if m_diff >= 30:
    m_diff -= 30

m3 = m1 + m_diff
h3 = h1 + h_diff

if m3 >= 60:
    m3 -= 60
    h3 += 1

print(str(int(h3)).zfill(2) + ':' + str(int(m3)).zfill(2))
