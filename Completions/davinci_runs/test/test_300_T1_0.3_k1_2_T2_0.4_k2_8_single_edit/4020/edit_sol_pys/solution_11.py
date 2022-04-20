

h1, m1 = input().split(':') # input time 1
h2, m2 = input().split(':') # input time 2

h1 = int(h1) # convert time 1 hours to integer
m1 = int(m1) # convert time 1 minutes to integer
h2 = int(h2) # convert time 2 hours to integer
m2 = int(m2) # convert time 2 minutes to integer

if m1 == m2: # if time 1 minutes == time 2 minutes
    if h1 == h2: # if time 1 hours == time 2 hours
        print(str(h1).zfill(2) + ':' + str(m1).zfill(2)) # print time 1
    else:
        print(str(h1 + 1).zfill(2) + ':' + str(m1).zfill(2)) # print time 1 + 1 hour
else:
    if h1 == h2: # if time 1 hours == time 2 hours
        print(str(h1).zfill(2) + ':' + str(int((m1 + m2) / 2)).zfill(2)) # print time 1 + time 2 minutes / 2
    else:
        print(str(h1 + 1).zfill(2) + ':' + str(int((m1 + m2) / 2)).zfill(2)) # print time 1 + 1 hour + time 2 minutes / 2
