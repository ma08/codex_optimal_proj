

h1, m1 = input().split(":")
h2, m2 = input().split(":")

h1 = int(h1)
h2 = int(h2)
m1 = int(m1)
m2 = int(m2)

if m1 == m2:
    h3 = h1 + (h2 - h1) // 2
    m3 = m1
else:
    h3 = h1 + (h2 - h1) // 2
    m3 = m1 + (m2 - m1) // 2
    if m3 >= 60:
        h3 += 1
        m3 -= 60

print("%02d:%02d" % (h3, m3))