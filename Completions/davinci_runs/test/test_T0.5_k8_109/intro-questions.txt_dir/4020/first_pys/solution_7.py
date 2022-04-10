

h1, m1 = map(int, input().split(':'))
h2, m2 = map(int, input().split(':'))

m_total = (h2 - h1) * 60 + m2 - m1
m_mid = m_total / 2

h_mid = h1 + m_mid // 60
m_mid = m1 + m_mid % 60

if m_mid >= 60:
    h_mid += 1
    m_mid -= 60

print("{:02d}:{:02d}".format(int(h_mid), int(m_mid)))