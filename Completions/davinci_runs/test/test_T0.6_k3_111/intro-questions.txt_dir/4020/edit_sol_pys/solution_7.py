h1, m1 = map(int, input().split(':'))
h2, m2 = map(int, input().split(':'))

m_difference = (m2 - m1) / 2

h_difference = (h2 - h1) / 2
if m_difference >= 30:
    h_difference += 0.5

if m_difference >= 30:
    m_difference -= 30

m3 = m1 + m_difference
h3 = h1 + h_difference

if m3 >= 60:
    m3 -= 60
    h3 += 1

print(str(int(h3)).zfill(2) + ':' + str(int(m3)).zfill(2))
