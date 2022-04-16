

h1, m1 = map(int, input().split(':')) #input of first time
h2, m2 = map(int, input().split(':')) #input of second time

m3 = (m1 + m2) // 2 #calculation of middle minute
h3 = h1 + (m1 + m2) // 120 #calculation of middle hour

if h3 > 23:
    h3 -= 24

print('{:02}:{:02}'.format(h3, m3))
