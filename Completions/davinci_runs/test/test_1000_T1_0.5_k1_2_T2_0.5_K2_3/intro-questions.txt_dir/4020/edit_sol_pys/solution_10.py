
h1, m1 = map(int, input().split(':')) #first time
h2, m2 = map(int, input().split(':')) #second time
m3 = (m1 + m2) // 2 #middle minute
h3 = h1 + (m1 + m2) // 120
if h3 > 23: #if hour is more than 23
    h3 -= 24
print('{:02}:{:02}'.format(h3, m3))
