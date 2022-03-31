h1, m1 = map(int, input().split(':')
h2, m2 = map(int, input().split(':')

if m1 % 2 == 0:
    m_mid = m1 + ((m2 - m1) // 2
else:
    m_mid = m1 + ((m2 - m1) // 2) + 1 

h_mid = h1 + ((m_mid - m1) // 60

print(f'{h_mid:02d}:{m_mid:02d}'
