

h1, m1 = map(int, input().split(':')) #h1, m1 = 12:00
h2, m2 = map(int, input().split(':')) #h2, m2 = 12:00

m3 = (m1 + m2) // 2 #m3 = 12:00
h3 = h1 + (m1 + m2) // 120 #h3 = 12:00

if h3 > 23:
    h3 -= 24

print('{:02}:{:02}'.format(h3, m3))
