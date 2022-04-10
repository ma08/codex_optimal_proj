

h1, m1 = input().split(':')
h2, m2 = input().split(':')

h1, h2, m1, m2 = int(h1), int(h2), int(m1), int(m2)

# print(h1, m1)
# print(h2, m2)

if m1 == m2:
    print(str(h1).zfill(2) + ':' + str(m1).zfill(2))
elif m1 < m2:
    if m1 % 2 == 0:
        print(str(h1).zfill(2) + ':' + str(m1+1).zfill(2))
    else:
        print(str(h1).zfill(2) + ':' + str(m1-1).zfill(2))
elif m1 > m2:
    if m2 % 2 == 0:
        print(str(h2).zfill(2) + ':' + str(m2+1).zfill(2))
    else:
        print(str(h2).zfill(2) + ':' + str(m2-1).zfill(2))