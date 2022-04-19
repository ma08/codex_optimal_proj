
h1, m1 = input().split(':')
h2, m2 = input().split(':')

h1 = int(h1)
m1 = int(m1)
h2 = int(h2)
m2 = int(m2)

if m1 == m2 and h1 == h2:
    print(str(h1).zfill(2) + ':' + str(m1).zfill(2))
elif m1 == m2:
    if h1 == h2:
        print(str(h1 + 1).zfill(2) + ':' + str(int((m1 + m2) / 2)).zfill(2))
    else:
        print(str(h1 + 1).zfill(2) + ':' + str(m1).zfill(2))
else:
    print(str(h1 + 1).zfill(2) + ':' + str(int((m1 + m2) / 2)).zfill(2))
