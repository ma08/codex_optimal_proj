
#-----main-----

h1, m1 = map(int, input().split(':')) # input 1
h2, m2 = map(int, input().split(':')) # input 2

if m1 == m2: # if minutes are equal
    h3 = h1
    m3 = m1
elif m1 < m2: # if minutes of input 1 is less than minutes of input 2
    h3 = h1
    m3 = (m1 + m2) // 2
else: # if minutes of input 1 is greater than minutes of input 2
    h3 = h1 + 1
    m3 = (m1 + m2) // 2

print('{:02d}:{:02d}'.format(h3, m3))
