

h1, m1 = map(int, input().split(':', 2))
h2, m2 = map(int, input().split(':', 2))

m3 = (m1 + m2) // 2
h3 = h1 + (m1 + m2) // 120

if h3 > 23:
    h3 -= 24

print('{:02}:{:02}'.format(h3, m3))
