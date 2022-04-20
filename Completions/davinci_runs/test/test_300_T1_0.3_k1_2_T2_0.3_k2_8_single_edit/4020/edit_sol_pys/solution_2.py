

h1, m1 = input().split(':') # input time 1
h2, m2 = input().split(':') # input time 2

h1 = int(h1) # convert to int
m1 = int(m1)
h2 = int(h2)
m2 = int(m2)

if m1 == m2: # if minutes are equal
    if h1 == h2: # if hours are equal
        print(str(h1).zfill(2) + ':' + str(m1).zfill(2))
    else: # if hours are not equal
        print(str(h1 + 1).zfill(2) + ':' + str(m1).zfill(2))
else: # if minutes are not equal
    if h1 == h2: # if hours are equal
        print(str(h1).zfill(2) + ':' + str(int((m1 + m2) / 2)).zfill(2))
    else:
        print(str(h1 + 1).zfill(2) + ':' + str(int((m1 + m2) / 2)).zfill(2))
